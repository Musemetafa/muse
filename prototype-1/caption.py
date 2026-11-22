"""Word-level captions for a prototype narration track (faster-whisper tiny.en).

Transcribes the mixed narration WAV with word timestamps, computes WER
against the known script (all narration parts concatenated), and writes
<id>-words.json next to the WAV. Must run in the inspection venv
(av==12.3.0 pinned — do not upgrade PyAV).
"""
import json
import os
import re
import sys
import time
import resource


def norm(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9' ]", " ", s)
    return s.split()


def wer(ref_words, hyp_words):
    n, m = len(ref_words), len(hyp_words)
    d = list(range(m + 1))
    for i in range(1, n + 1):
        prev, d[0] = d[0], i
        for j in range(1, m + 1):
            cur = d[j]
            d[j] = min(d[j] + 1, d[j - 1] + 1,
                       prev + (0 if ref_words[i - 1] == hyp_words[j - 1] else 1))
            prev = cur
    return d[m], d[m] / max(n, 1)


def main():
    wav_path = sys.argv[1]
    script_path = sys.argv[2]
    with open(script_path) as f:
        spec = json.load(f)
    vid = spec["id"]
    base = os.path.dirname(os.path.abspath(script_path))
    ref_text = " ".join(
        p["speak"] for b in spec["beats"] for p in b.get("parts", []))
    ref = norm(ref_text)

    from faster_whisper import WhisperModel
    t0 = time.time()
    model = WhisperModel("tiny.en", device="cpu", compute_type="int8")
    t_load = time.time() - t0
    t0 = time.time()
    segments, info = model.transcribe(wav_path, word_timestamps=True,
                                      beam_size=5, language="en")
    segs = list(segments)
    t_trans = time.time() - t0
    text = " ".join(s.text for s in segs).strip()
    hyp = norm(text)
    dist, rate = wer(ref, hyp)
    words = [{"word": w.word, "start": float(w.start), "end": float(w.end)}
             for s in segs for w in (s.words or [])]
    out = {
        "id": vid,
        "model": "tiny.en",
        "load_seconds": t_load,
        "transcribe_seconds": t_trans,
        "detected_language": info.language,
        "language_probability": float(info.language_probability),
        "transcript": text,
        "reference_words": len(ref),
        "hypothesis_words": len(hyp),
        "wer": rate,
        "wer_edits": dist,
        "words": words,
        "peak_rss_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0,
    }
    with open(os.path.join(base, f"{vid}-words.json"), "w") as f:
        json.dump(out, f, indent=2)
    print(f"[{vid}] load {t_load:.1f}s | transcribe {t_trans:.1f}s | "
          f"lang {info.language} p={info.language_probability:.2f}", flush=True)
    print(f"[{vid}] WER {rate:.3f} ({dist} edits / {len(ref)} ref words) | "
          f"words with timestamps {len(words)} | peak RSS "
          f"{out['peak_rss_mb']:.0f} MB", flush=True)
    print(f"[{vid}] transcript: {text!r}", flush=True)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
