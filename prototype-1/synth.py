"""Prototype narration synthesis with Kokoro-82M (kokoro-onnx).

Reads a prototype script JSON, synthesizes every narration part with
af_heart (PROVISIONAL voice — Mohamed has not answered the listening
test yet), and mixes the full audio track:
  - narration segments (leading/trailing silence trimmed to 0.15 s)
  - 0.25 s gaps between parts, 0.35 s gaps between beats
  - think beats: a tick every second over a quiet bed (never dead air)
  - answer beats: a short ding at the reveal
  - a quiet 110+165 Hz bed across the whole track (~-40 dB) so the
    audio track is never empty (silencedetect must find no silence)

Outputs (all under the script's directory, never /tmp):
  <id>-narration.wav   mixed audio track (24 kHz mono PCM16)
  <id>-timings.json    beat/part start/end times (seconds)
  segments/<id>/beatXX_partY.wav  individual narration parts (evidence)
"""
import json
import os
import sys
import time
import resource

import numpy as np
import soundfile as sf

MODEL = os.path.expanduser("~/workspace/inspection/kokoro/kokoro-v1.0.onnx")
VOICES = os.path.expanduser("~/workspace/inspection/kokoro/voices-v1.0.bin")
SR = 24000
VOICE = "af_heart"
PART_GAP = 0.25
BEAT_GAP = 0.35
TRIM_THRESH = 0.01
TRIM_KEEP = 0.15


def trim_silence(x):
    """Trim leading/trailing samples below threshold, keeping TRIM_KEEP s."""
    if len(x) == 0:
        return x
    above = np.where(np.abs(x) > TRIM_THRESH)[0]
    if len(above) == 0:
        return x
    keep_n = int(TRIM_KEEP * SR)
    start = max(0, above[0] - keep_n)
    end = min(len(x), above[-1] + 1 + keep_n)
    return x[start:end]


def main():
    script_path = sys.argv[1]
    with open(script_path) as f:
        spec = json.load(f)
    base = os.path.dirname(os.path.abspath(script_path))
    vid = spec["id"]
    segdir = os.path.join(base, "segments", vid)
    os.makedirs(segdir, exist_ok=True)

    t0 = time.time()
    from kokoro_onnx import Kokoro
    kokoro = Kokoro(MODEL, VOICES)
    print(f"model load: {time.time() - t0:.1f}s", flush=True)

    beats_out = []
    total_synth = 0.0
    total_words = 0
    for bi, beat in enumerate(spec["beats"]):
        bout = {"kind": beat["kind"], "parts": []}
        if "n" in beat:
            bout["n"] = beat["n"]
            bout["total"] = beat["total"]
        if beat["kind"] == "think":
            bout["seconds"] = beat["seconds"]
            beats_out.append(bout)
            continue
        for pi, part in enumerate(beat["parts"]):
            total_words += len(part["speak"].split())
            t1 = time.time()
            out = kokoro.create(part["speak"], voice=VOICE, speed=1.0, lang="en-us")
            samples = out[0] if isinstance(out, tuple) else out
            samples = np.asarray(samples, dtype=np.float32)
            t_synth = time.time() - t1
            total_synth += t_synth
            samples = trim_silence(samples)
            dur = len(samples) / SR
            seg_name = f"beat{bi:02d}_part{pi}.wav"
            sf.write(os.path.join(segdir, seg_name), samples, SR)
            rms = float(np.sqrt(np.mean(samples ** 2))) if len(samples) else 0.0
            peak = float(np.max(np.abs(samples))) if len(samples) else 0.0
            print(f"beat {bi} part {pi}: synth {t_synth:.1f}s | audio {dur:.2f}s | "
                  f"RTF {t_synth / max(dur, 0.01):.2f} | rms {rms:.3f} peak {peak:.3f} | {seg_name}",
                  flush=True)
            bout["parts"].append({"speak": part["speak"], "dur": dur, "seg": seg_name})
        beats_out.append(bout)

    # --- lay out the timeline ---
    cursor = 0.0
    for bi, (beat, bout) in enumerate(zip(spec["beats"], beats_out)):
        if beat["kind"] == "think":
            bout["start"] = cursor
            bout["end"] = cursor + beat["seconds"]
            cursor = bout["end"]
        else:
            bout["start"] = cursor
            for pi, p in enumerate(bout["parts"]):
                if pi > 0:
                    cursor += PART_GAP
                p["start"] = cursor
                p["end"] = cursor + p["dur"]
                cursor = p["end"]
            bout["end"] = cursor
        if bi < len(spec["beats"]) - 1:
            cursor += BEAT_GAP
    total_dur = cursor

    # --- mix ---
    n_total = int(round(total_dur * SR))
    mix = np.zeros(n_total, dtype=np.float32)
    tarr = np.arange(n_total, dtype=np.float64) / SR
    mix += (0.011 * np.sin(2 * np.pi * 110 * tarr)
            + 0.007 * np.sin(2 * np.pi * 165 * tarr)).astype(np.float32)
    for bout in beats_out:
        for p in bout.get("parts", []):
            seg, _ = sf.read(os.path.join(segdir, p["seg"]), dtype="float32")
            s0 = int(round(p["start"] * SR))
            s1 = min(n_total, s0 + len(seg))
            mix[s0:s1] += seg[: s1 - s0]
    for bout in beats_out:
        if bout["kind"] == "think":
            t = bout["start"] + 0.5
            while t < bout["end"] - 0.1:
                i0 = int(round(t * SR))
                n = int(0.07 * SR)
                env = np.exp(-np.arange(n) / (0.015 * SR))
                blip = (0.30 * np.sin(2 * np.pi * 1250 * np.arange(n) / SR) * env).astype(np.float32)
                mix[i0:i0 + n] += blip
                t += 1.0
        if bout["kind"] == "answer":
            i0 = int(round(bout["start"] * SR))
            n = int(0.5 * SR)
            env = np.exp(-np.arange(n) / (0.12 * SR))
            ding = (0.35 * (np.sin(2 * np.pi * 880 * np.arange(n) / SR)
                            + 0.5 * np.sin(2 * np.pi * 1320 * np.arange(n) / SR)) * env).astype(np.float32)
            mix[i0:i0 + n] += ding
    peak = float(np.max(np.abs(mix)))
    if peak > 0.95:
        mix *= 0.95 / peak
        peak = 0.95
    mix_rms = float(np.sqrt(np.mean(mix ** 2)))
    wav_path = os.path.join(base, f"{vid}-narration.wav")
    sf.write(wav_path, mix, SR)
    timings = {
        "id": vid,
        "voice": VOICE,
        "voice_provisional": True,
        "sample_rate": SR,
        "total_duration": total_dur,
        "total_synth_seconds": total_synth,
        "total_words": total_words,
        "mix_peak": peak,
        "mix_rms": mix_rms,
        "peak_rss_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
        "beats": beats_out,
    }
    with open(os.path.join(base, f"{vid}-timings.json"), "w") as f:
        json.dump(timings, f, indent=2)
    print(f"TOTAL duration {total_dur:.2f}s | words {total_words} | "
          f"synth {total_synth:.1f}s (RTF {total_synth / max(total_dur, 0.01):.2f}) | "
          f"mix peak {peak:.3f} rms {mix_rms:.4f} | peak RSS "
          f"{timings['peak_rss_mb']:.0f} MB", flush=True)
    print(f"wrote {wav_path} ({os.path.getsize(wav_path)} bytes)", flush=True)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
