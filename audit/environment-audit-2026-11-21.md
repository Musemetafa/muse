# تدقيق بيئة التشغيل — تقرير قراءة فقط

**تاريخ التدقيق:** 2026-11-21 23:39 UTC (المنطقة الزمنية للعميل: Africa/Casablanca)
**النطاق:** تدقيق قراءة فقط. لم يُستخدم apt أو pip أو npm أو أي مثبّت، ولم يُنزَّل أي برنامج أو نموذج، ولم يُغيَّر أي إعداد أو ملف نظام، ولم يُنشأ أي حساب، ولم يُسجَّل في أي موقع، ولم يُشترَ أي شيء.
**ما لم يُقرأ:** لم تُقرأ رسائل بريد ولا ملفات خاصة بالمستخدم، ولم تُعرض أي كلمات سر أو مفاتيح أو رموز. أسماء متغيرات البيئة فقط ذُكرت، دون قيمها.
**الملفات المؤقتة للاختبار:** أُنشئت ملفات اختبار في `/tmp` فقط (`audit_test.mp4`، `audit_test.png`، `audit_hello.c`، `audit_hello`) ثم حُذفت جميعها. أمر الحذف أكّد عدم بقائها: `ls: cannot access '/tmp/audit_*': No such file or directory`.

---

## 1. أين نعمل فعلياً

**الخلاصة المؤكدة:** ليست جهازاً محلياً فيزيائياً في منزل المستخدم. هي آلة افتراضية Linux في بيئة تشغيل مُدارة (Hatch runtime)، على KVM.

### ما تأكدت منه عملياً

- الأمر: `uname -a`
  - المخرج:
    ```
    Linux htch-runtime 7.0.0-44-generic #1 SMP PREEMPT_DYNAMIC Fri Nov  6 01:23:31 UTC 2026 x86_64 x86_64 x86_64 GNU/Linux
    ```
- الأمر: `cat /etc/os-release`
  - المخرج (مختصر):
    ```
    PRETTY_NAME="Ubuntu 24.04.5 LTS"
    NAME="Ubuntu"
    VERSION_ID="24.04"
    VERSION="24.04.5 LTS (Noble Numbat)"
    ID=ubuntu
    IMAGE_ID="hatch-image"
    IMAGE_VERSION="0.1.46"
    ```
- الأمر: `hostname; whoami; id; pwd; uptime`
  - المخرج:
    ```
    htch-runtime
    root
    uid=0(root) gid=0(root) groups=0(root)
    /home/hatch
    23:39:23 up  1:33,  0 user,  load average: 0.16, 0.25, 0.22
    ```
- الأمر: `lscpu` (مختصر)
  - المخرج:
    ```
    Architecture: x86_64
    CPU(s): 4
    Vendor ID: AuthenticAMD
    Model name: AMD EPYC 9D25 126-Core Processor
    Thread(s) per core: 1
    Core(s) per socket: 4
    Hypervisor vendor: KVM
    Virtualization type: full
    L1d cache: 96 KiB (2 instances)
    L2 cache: 2 MiB (2 instances)
    L3 cache: 32 MiB (1 instance)
    ```
  - الأعلام تشمل `avx`, `avx2`, `avx512f`, `avx512bw`, `avx512vl`, `fma`, `aes`, `sha_ni`.
- الأمر: `nproc`
  - المخرج: `4`
- الأمر: `free -h` و `grep MemTotal /proc/meminfo`
  - المخرج:
    ```
    Mem: 7.7Gi total, 7.2Gi used, 173Mi free, 673Mi buff/cache, 574Mi available
    Swap: 1.0Gi total, 335Mi used, 688Mi free
    MemTotal: 8124900 kB
    MemAvailable: 572396 kB
    ```
  - ملاحظة: حد الذاكرة المشتركة الذي يبلّغ عنه وقت التشغيل هو `sharedMemoryLimitBytes: 6442450944` (نحو 6 GiB)، وحد المعالج المشترك هو `sharedCpuMillis: 1500` (1.5 وحدة معالج مشتركة)، رغم أن `nproc` يظهر 4. هذا تناقض ظاهري يجب عدم تجاهله: العدد الاسمي للأنوية ليس هو الحصة الفعلية.
- الأمر: `df -h`
  - المخرج (مختصر):
    ```
    overlay 7.5G 110M 7.4G 2% /
    tmpfs 512M 92K 512M 1% /tmp
    tmpfs 794M 0 794M 0% /dev/shm
    /dev/mapper/rv 150G 134M 149G 1% /home/hatch
    ```
  - أي: التخزين الكبير الوحيد هو `/home/hatch` (149G متاحة). الجذر 7.5G فقط، و`/tmp` 512M فقط.
- الأمر: `cat /proc/loadavg` و `cat /proc/pressure/memory`
  - المخرج:
    ```
    0.28 0.26 0.22 1/440 15467
    some avg10=0.74 avg60=0.16 avg300=0.03
    full avg10=0.74 avg60=0.16 avg300=0.03
    ```
  - ضغط الذاكرة لحظياً غير صفري، والذاكرة المتاحة وقت التدقيق كانت نحو 560 MiB فقط.

### معالج الرسوميات — مؤكد غيابه بالأدلة

- الأمر: `nvidia-smi`
  - المخرج: `/bin/bash: line 1: nvidia-smi: command not found` — exit `127`
- الأمر: `ls -l /dev/nvidia*` و `ls -l /dev/dri/`
  - المخرج:
    ```
    ls: cannot access '/dev/nvidia*': No such file or directory
    ls: cannot access '/dev/dri/': No such file or directory
    ```
- الأمر: `command -v lspci vulkaninfo glxinfo`
  - المخرج: كلها `NOT FOUND`. أي لا يمكن تأكيد أي GPU عبر `lspci` أصلاً، لأن الأداة نفسها غير مثبتة، لكن غياب `/dev/dri` و`/dev/nvidia*` دليل قوي على عدم وجود GPU مكشوفة.
- الأمر: `ls /dev/snd` و `ls /dev/video*`
  - المخرج: `ls: cannot access '/dev/snd': No such file or directory` و `ls: cannot access '/dev/video*': No such file or directory`
  - أي: لا جهاز صوت ولا جهاز التقاط فيديو/كاميرا.

---

## 2. ما الأدوات والبرامج والنماذج المتاحة حالياً؟

### أ. ما تأكدت منه عملياً — يعمل فعلاً، لا مجرد ظهور في قائمة

| الأداة | الأمر | المخرج الفعلي المختصر |
|---|---|---|
| ffmpeg | `ffmpeg -version` | `ffmpeg version 8.1.2 Copyright (c) 2000-2026` — `built with gcc 13` |
| ffprobe | `ffprobe -version` | `ffprobe version 8.1.2` |
| ترميز فعلي بـ ffmpeg | `ffmpeg -y -f lavfi -i testsrc=duration=1:size=640x360:rate=30 -f lavfi -i sine=frequency=440:duration=1 -c:v libx264 -pix_fmt yuv420p -c:a aac -shortest /tmp/audit_test.mp4` | `ffmpeg encode exit:0` — الملف `22K` — `ffprobe` أكّد: `Video: h264 (High), yuv420p, 640x360, 30 fps` و `Audio: aac (LC), 44100 Hz, mono` — المدة `00:00:01.00` |
| مشفرات ffmpeg | `ffmpeg -encoders \| grep libx264/libx265/libvpx/libaom/libsvtav1` | `libx264`, `libx264rgb`, `libx265`, `libvpx`, `libvpx-vp9`, `libaom-av1`, `libsvtav1`, `aac`, `libmp3lame`, `libopus` |
| فلاتر ffmpeg | `ffmpeg -filters \| grep drawtext/overlay/fade` | `drawtext`, `overlay`, `fade`, `afade`, `acrossfade` موجودة |
| Python | `python3 --version` | `Python 3.12.3` |
| Python — إنشاء صورة | `python3 -c "from PIL import Image; ..."` | `PIL OK (320, 180)` — الملف `604` بايت |
| numpy / Pillow / requests | `python3 -c "import numpy/PIL/requests"` | `numpy: 1.26.4`، `PIL: 10.2.0`، `requests: 2.31.0` |
| Node.js | `node --version` و `node -e "console.log(...)"` | `v24.22.1` — `node OK v24.22.1` |
| npm | `npm --version` | `10.9.4` |
| Bun | `bun --version` | `1.4.4` |
| gcc / g++ | `gcc --version` | `gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0` |
| تجميع وتشغيل C | `gcc /tmp/audit_hello.c -o /tmp/audit_hello && /tmp/audit_hello` | `gcc exit:0` — المخرج `hello audit` — `run exit:0` |
| git | `git --version` | `git version 2.43.0` |
| curl | `curl --version \| head -n1` | `curl 8.5.0 (x86_64-pc-linux-gnu) libcurl/8.5.0 OpenSSL/3.0.13` |
| wget | `wget --version \| head -n1` | `GNU Wget 1.21.4 built on linux-gnu.` |
| jq | `jq --version` | `jq-1.7` |
| make / cmake | `command -v make cmake` | `/usr/bin/make`، `/usr/bin/cmake` |
| Xvfb | `command -v Xvfb xvfb-run` | `/usr/bin/Xvfb`، `/usr/bin/xvfb-run` |
| الخطوط | `fc-list \| head` | `Noto Sans`, `Noto Serif`, `Noto Sans Arabic` وغيرها؛ ومجلدات `dejavu`, `liberation`, `noto` في `/usr/share/fonts/truetype/` |

حزم Python المثبتة (من `pip3 list`، مختصر): `numpy 1.26.4`، `pillow 10.2.0`، `pandas 2.1.4+dfsg`، `matplotlib 3.6.3`، `SciPy 1.11.4`، `requests 2.31.0`، `PyYAML 6.0.1`، `openpyxl 3.1.2`، `python-docx 3.1.2` — القائمة الكاملة في المخرج الأصلي 46 حزمة تقريباً، ولا تشمل أي حزمة ذكاء اصطناعي للفيديو.

### ب. موجود في المسار لكنه لم يُختبر تشغيله فعلياً في هذا التدقيق

- `pip3` / `pip`: الإصدار `pip 24.0 from /usr/lib/python3/dist-packages/pip (python 3.12)` — ظهور الإصدار فقط، ولم يُستخدم للتثبيت (محظور في هذا التدقيق).
- `tar`, `unzip`, `zip`: موجودة في المسار فقط، لم تُختبر بفك ضغط فعلي.
- `make`, `cmake`: موجودة فقط، لم يُختبر بناء مشروع بهما.
- `Xvfb` / `xvfb-run`: موجودة فقط، لم يُختبر تشغيل خادم X افتراضي.
- `systemctl` / `systemd-run`: `systemctl is-system-running` أعاد `running` — لكن لم يُختبر إنشاء خدمة أو جدولة.
- `media-generation --help`: يعمل ويعرض وصفاً: `Generate images and videos via Meta's media generation API.` — التوليد الفعلي لم يُختبر.
- `tts --help`: يعمل ويعرض وصفاً: `Text-to-speech via Meta Shortwave API.` — الصوت الافتراضي في المساعدة `avocado_v2:MAI_03`، اللغة الافتراضية `en`، الصيغة الافتراضية `mp3` — التوليد الفعلي لم يُختبر.
- `bun`: الإصدار فقط، لم يُختبر تشغيل مشروع به.

### ج. غير موجود — `command not found` أو استيراد فاشل

- الأوامر غير الموجودة:
  ```
  python (بدون 3)، convert، magick، identify، go، rustc، cargo، java،
  chromium، chromium-browser، google-chrome، firefox،
  ollama، whisper، faster-whisper، yt-dlp، docker، podman،
  lspci، vulkaninfo، glxinfo، display، ffmpegthumbnailer،
  sox، lame، espeak، espeak-ng، festival، tesseract،
  pulseaudio، pactl، aplay، arecord، cron، crond، snap، flatpak
  ```
- وحدات Python غير المثبتة (استيرادها أعاد `Traceback`):
  ```
  cv2، torch، transformers، diffusers، moviepy، imageio، pydub
  ```
- لا نماذج محلية وُجدت في بحث على مستوى النظام:
  - الأمر: `find /opt /usr/local /usr/share -maxdepth 3 \( -iname "*ollama*" -o -iname "*whisper*" -o -iname "*stable-diffusion*" -o -iname "*huggingface*" \)`
  - المخرج: لا شيء. ولم يُفتَّش ذاكرة المستخدم المؤقتة عمداً، فلا أدّعي شيئاً عنها.
- `npm list -g --depth=0`:
  ```
  /usr/lib
  `-- (empty)
  ```
  أي لا حزم Node عالمية مثبتة.

---

## 3. ما قدراتك الفعلية؟

### الطرفية (Terminal) — مؤكدة

- الأمر: `pwd; whoami; id`
  - المخرج: `/home/hatch` — `root` — `uid=0(root) gid=0(root) groups=0(root)`
- الأمر: `sudo -n true; echo exit:$?` و `sudo -n -l`
  - المخرج:
    ```
    sudo -n true exit:0
    User root may run the following commands on htch-runtime:
        (ALL : ALL) ALL
    ```
  - أي: نحن root أصلاً، وsudo بلا كلمة سر يعمل. هذا لا يلغي حدود وقت التشغيل المشتركة (1.5 CPU / ~6 GiB).
- الأمر: `systemctl is-system-running`
  - المخرج: `running`
- الصدفة: `/bin/bash` موجود، و`/bin/sh -> dash`.

### الملفات — مؤكدة جزئياً، ومقيدة جزئياً

- قراءة ملفات النظام عبر الطرفية: مؤكدة. مثال: `cat /etc/os-release` نجح.
- الكتابة في `/tmp`: مؤكدة باختبار ffmpeg وPIL وgcc، ثم حُذفت الملفات.
- الكتابة في `/home/hatch`: مؤكدة بالاختبار دون إنشاء ملف: `test -w /home/hatch && echo "/home/hatch writable"` أعاد `/home/hatch writable`. وكذلك `/tmp writable`، و`/` و`/usr` أعادا `writable` كـ root — لكن هذا لا يعني أنهما مكان تخزين آمن؛ الجذر صغير (7.5G) و`/tmp` مؤقت (512M) وكل ما خارج `~` يُعامل كزائل وفق قواعد وقت التشغيل.
- أداة `muse.read`: **فشلت** في قراءة `/etc/os-release`:
  ```
  path '/etc/os-release' is outside the home directory and /tmp
  ```
  أي: أداة القراءة الخاصة بالوكيل مقيدة بـ `~` و`/tmp`، بينما الطرفية تستطيع قراءة ملفات النظام. هذا فرق مهم بين قدرة الطرفية وقدرة أداة الملفات.
- أدوات الكتابة/التحرير الخاصة بالوكيل (`muse.write` / `muse.edit`): لم تُختبر في هذا التدقيق إلا لكتابة هذا التقرير نفسه في `~/workspace/audit/`، وهو خارج نطاق الاختبار الوظيفي للفيديو. لا أدّعي اختباراً أوسع لها هنا.

### البرمجة — مؤكدة للغات المذكورة

- Python 3.12.3: تشغيل `python3 -c "print('python OK')"` نجح.
- Node v24.22.1 وBun 1.4.4: تشغيل Node نجح. Bun بالإصدار فقط.
- C عبر gcc 13.3.0: تجميع وتشغيل `hello audit` نجح.
- Go / Rust / Java: غير موجودة أصلاً (انظر القسم 2ج).

### المتصفح — مؤكد جزئياً، ومحدود كوكيل فرعي

- لا متصفح محلي في الطرفية: `chromium`، `chromium-browser`، `google-chrome`، `firefox` كلها `NOT FOUND`.
- لا شاشة: `DISPLAY=<empty>`، و`XDG_SESSION_TYPE=<empty>`.
- أداة البحث النصي `browser.search`: **مُختبرة ونجحت** — أُجري بحث تجريبي عن ffmpeg وأعاد نتائج نصية.
- أداة جلب نص الصفحة `browser.open`: **مُختبرة ونجحت في جلب نص** — أعادت نص صفحة عن ffmpeg (704 سطور). ملاحظة دقة: الصفحة المُعادة لم تطابق تماماً نتيجة البحث رقم 0 المتوقعة، فلا ينبغي الاعتماد على تطابق الفهرس حرفياً دون تحقق.
- **غير مُختبر / غير متاح لهذا الوكيل الفرعي:** التحكم في متصفح حي (نقر، تسجيل دخول، تعبئة نماذج، شراء، تنقّل تفاعلي). هذا العمل يتطلب وكيلاً آخر، وفق تعليمات النظام. لا أدّعي زيارة موقع حي.

### الإنترنت والوصول إلى المستودعات — مؤكد جزئياً

- الأمر: `curl -s -o /dev/null -w "%{http_code}" -I https://example.com` و`https://github.com` و`https://pypi.org`
  - المخرج:
    ```
    example.com:200 time:0.336837s
    github.com:200 time:0.798806s
    pypi.org:200
    ```
- الأمر: `python3 -c "import urllib.request; print(urllib.request.urlopen('https://example.com', timeout=10).status)"`
  - المخرج: `200`
- الأمر: `getent hosts example.com` و`github.com`
  - المخرج:
    ```
    198.18.234.221 example.com
    198.18.234.222 github.com
    ```
  - هذان العنوانان ليسا العناوين العامة المعتادة لهذين النطاقين؛ هذا يشير إلى اعتراض عبر وكيل/بروكسي. أسماء متغيرات البيئة تشمل `HTTP_PROXY`، `HTTPS_PROXY`، `http_proxy`، `https_proxy`، `NO_PROXY`، `no_proxy` — قيمها لم تُعرض عمداً.
- **لم يُختبر:** `git clone` أو `git ls-remote` أو تنزيل ملف كبير أو بث أو واجهات منصات. وصول GitHub عبر HEAD لا يثبت نجاح الاستنساخ.

### التثبيت — لم يُختبر بسبب الحظر الصارم في هذه المهمة

- الأمر: `command -v apt apt-get dpkg`
  - المخرج: `/usr/bin/apt`، `/usr/bin/apt-get`، `/usr/bin/dpkg` موجودة. و`snap` و`flatpak` غير موجودتين.
- لكن: **لم يُستخدم أي مثبّت في هذا التدقيق.** لا أدّعي أن التثبيت يعمل، ولا أن الشبكة أو الصلاحيات تسمح به عملياً، ولا أن حزمة معينة ستثبت بنجاح. هذا سؤال لم يُختبر عمداً.

---

## 4. ما الصلاحيات والاتصالات المتاحة فعلاً؟ وما حدودها؟

### ما تأكدت منه عملياً

- نحن `root`، و`sudo -n` بلا كلمة سر يعمل، و`sudo -l` يظهر `(ALL : ALL) ALL`.
- `/home/hatch` قابلة للكتابة، ومساحتها 150G (149G متاحة).
- `systemd` يعمل (`running`).
- الإنترنت عبر `curl` وPython يعمل لمواقع الاختبار الثلاثة أعلاه.

### ما يبدو متاحاً لكنه لم يُختبر — لا تفترضه

- موصلات (Connectors): يوجد 143 مجلداً في `/opt/hatch/connectors`، منها `gmail`، `instagram`، `instagram_messages`، `google_drive`، `google_docs`، `google_calendar`، `facebook_cli`، `meta_ads`، `opusclip`، `runway_mcp`، `vidiq_mcp`، `krea`، `luma` وغيرها. **وجود مجلد موصل ليس دليلاً على اتصال أو تفويض.** حالة الاتصال الفعلية لأي حساب لم تُتحقق في هذا التدقيق، لأن قراءة البريد أو حالة الحساب كانت محظورة في هذه المهمة.
- لا يوجد موصل TikTok في القائمة: بحث `grep -i -E "tiktok"` في قائمة الموصلات لم يُعد أي نتيجة (المطابقات الوحيدة في بحث ذي صلة كانت `gmail` و`instagram`). هذا لا يثبت استحالة الوصول إلى TikTok بطريقة أخرى، بل يثبت فقط غياب موصل مخصص ظاهر في هذه القائمة.
- أداتا `media-generation` و`tts`: هما واجهتا API خارجيتان من Meta (حسب نص `--help`)، وليستا نموذجين محليين. التوليد الفعلي لم يُختبر، والتكلفة والحصص والحدود غير معروفة في هذا التدقيق — لا تفترض أنها مجانية أو غير محدودة.
- أدوات الجدولة الخاصة بالوكيل (`cron` في Muse): لا يوجد ثنائي `cron`/`crond` محلي (`command -v cron crond` أعاد exit `1` بلا مخرج). الجدولة إن وُجدت فهي عبر أدوات وقت التشغيل، ولم تُختبر في هذا التدقيق.

### ما لا نملك القدرة أو الصلاحية للوصول إليه (بأدلة هذا التدقيق)

- GPU: لا `nvidia-smi`، لا `/dev/nvidia*`، لا `/dev/dri`.
- أجهزة صوت/فيديو: لا `/dev/snd`، لا `/dev/video*`.
- متصفح محلي: لا Chromium/Firefox/Chrome.
- نماذج ذكاء اصطناعي محلية: لا `torch`، لا `transformers`، لا `diffusers`، لا `ollama`، لا `whisper`، ولا ملفات نماذج وُجدت في البحث على مستوى النظام.
- تحكم حي في المتصفح لهذا الوكيل الفرعي: غير متاح وفق تعليمات النظام.
- قراءة ملفات خارج `~` و`/tmp` عبر أداة `muse.read`: مرفوضة برسالة صريحة (انظر القسم 3).
- البريد وملفات المستخدم الخاصة: لم تُقرأ في هذا التدقيق عمداً، فلا أدّعي أي معرفة بمحتواها أو حالة اتصالها من هذا التدقيق.

---

## 5. القيود والمخاطر التي اكتشفتها

1. **لا GPU إطلاقاً.** أي ترميز أو عرض أو توليد محلي سيكون على CPU فقط. هذا لا يمنع ffmpeg، لكنه يجعل العمل الثقيل بطيئاً.
2. **حصة CPU وذاكرة محدودة ومضغوطة.** `nproc` يظهر 4، لكن الحصة المشتركة المبلّغة هي 1.5 CPU و~6 GiB ذاكرة. وقت التدقيق كانت الذاكرة المتاحة نحو 572 MiB فقط، والـ Swap مستخدم (335 MiB)، وضغط الذاكرة `some avg10=0.74`. خطر الاختناق أو نفاد الذاكرة في المهام الثقيلة حقيقي، ولم يُختبر حدّه.
3. **تخزين مؤقت صغير جداً.** `/tmp` 512M فقط، والجذر 7.5G فقط. الملفات الوسيطة الكبيرة لا تصلح في `/tmp`؛ مكانها الوحيد الواسع هو `/home/hatch` (149G متاحة).
4. **لا نماذج محلية ولا أدوات ذكاء اصطناعي للفيديو.** لا `torch` ولا `transformers` ولا `diffusers` ولا `moviepy` ولا `cv2` ولا `ollama` ولا `whisper`. أي توليد أو نسخ أو تعرف صوتي محلي غير موجود حالياً — والبدائل الخارجية (مثل `media-generation` و`tts`) لم يُختبر توليدها الفعلي هنا.
5. **لا أدوات تحرير فيديو جاهزة ولا OCR ولا TTS محلي.** لا ImageMagick، لا SoX، لا `espeak`، لا `tesseract`، لا `moviepy`، لا `cv2`. المتاح فعلياً للفيديو هو ffmpeg/ffprobe + Pillow + كود مخصص — وهذا ما أُثبت فقط.
6. **لا موصل TikTok ظاهر.** لا يوجد موصل مخصص في قائمة الموصلات الـ 143. النشر أو الإدارة المباشرة عبر TikTok لم تُختبر ولم تُثبت في هذا التدقيق.
7. **الشبكة عبر بروكسي.** إجابات DNS للاختبار كانت عناوين وكيل (198.18.234.x)، وأسماء متغيرات البيئة تشير إلى موافقات على الخروج (egress approval) ومقابس Hatch. وصول HEAD إلى example.com وGitHub وPyPI يعمل، لكن الاستنساخ الكامل والتنزيلات الكبيرة وواجهات المنصات لم تُختبر، ولا يُفترض أنها غير مقيدة.
8. **لا `cron` محلي.** الجدولة الدورية تعتمد على أدوات وقت التشغيل، لا على `cron` في هذه الآلة.
9. **الاستمرارية محدودة بالمسار.** وفق قواعد وقت التشغيل، ما يبقى هو `~` فقط؛ `/tmp` ومسارات النظام زائلة. أي عمل يجب أن يعيش تحت `/home/hatch`.
10. **الصلاحية كـ root لا تلغي حدود الموارد.** `sudo ALL` لا يعني CPU أو ذاكرة غير محدودة؛ الحصة المشتركة تبقى 1.5 CPU / ~6 GiB.
11. **لا إدخال صوتي/مرئي حقيقي.** لا ميكروفون ولا كاميرا ولا جهاز صوت. أي صوت يجب أن يأتي من ملف خارجي أو من TTS عبر API (لم يُختبر توليده)، وأي لقطات يجب أن تأتي من ملفات أو توليد خارجي.

---

## 6. ملخص الفصل المطلوب

### ما تأكدت منه عملياً
- آلة افتراضية Ubuntu 24.04.5 LTS على KVM، اسم المضيف `htch-runtime`، معالج AMD EPYC 9D25، 4 أنوية اسمية، حصة فعلية مبلّغة 1.5 CPU، ذاكرة إجمالية 7.7 GiB مع ~0.56 GiB متاحة وقت التدقيق، تخزين `/home/hatch` 150G (149G متاحة).
- لا GPU، لا صوت، لا كاميرا، لا متصفح محلي، لا شاشة.
- ffmpeg 8.1.2 يعمل فعلياً (ترميز H.264 + AAC ناجح)، وPython 3.12.3 مع numpy/Pillow/requests يعمل، وNode 24.22.1 وBun 1.4.4 وgcc 13.3.0 يعمل (تجميع وتشغيل ناجح).
- الإنترنت يعمل لـ HEAD إلى example.com وGitHub وPyPI، وبحث الويب النصي وجلب نص الصفحة يعملان.
- نحن root مع sudo كامل، و`/home/hatch` قابلة للكتابة.

### ما يبدو متاحاً لكنه لم يُختبر
- `pip` و`apt` و`npm` موجودة كثنائيات، لكن التثبيت لم يُختبر (محظور في هذه المهمة).
- `media-generation` و`tts` تظهران `--help` وتشيران إلى API خارجية من Meta، لكن التوليد الفعلي لم يُختبر.
- 143 موصلاً في `/opt/hatch/connectors`، لكن حالة اتصال أي منها لم تُتحقق.
- `git` موجود وGitHub يرد على HEAD، لكن الاستنساخ لم يُختبر.
- `Xvfb` و`systemd` و`make`/`cmake` موجودة، لكن تشغيلها الوظيفي لم يُختبر.

### ما لا تملك القدرة أو الصلاحية للوصول إليه
- GPU، وأجهزة صوت/فيديو، ومتصفح محلي، ونماذج AI محلية، وأدوات TTS/STT/OCR محلية، وموصل TikTok ظاهر، وتحكم حي في المتصفح لهذا الوكيل الفرعي، وقراءة ملفات خارج `~`/`/tmp` عبر أداة `muse.read`، والبريد/الملفات الخاصة (لم تُقرأ عمداً).

### القيود والمخاطر
- انظر القسم 5 كاملاً. أبرزها: CPU مشتركة 1.5 وضغط ذاكرة فعلي، و`/tmp` 512M فقط، وغياب GPU والنماذج المحلية، والاعتماد على بروكسي وAPI خارجية غير مختبرة، وغياب موصل TikTok.

---

*نهاية التقرير. لم يُقترح في هذا التقرير أي بنية للمصنع ولا أي تقنية إنتاج، وفق المهمة.*
