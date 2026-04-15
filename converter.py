from faster_whisper import WhisperModel

model_size = "large-v3"

model = WhisperModel(
    "base",  # o "small" si tienes buen procesador
    device="cpu",
    compute_type="int8",  # int8 es más rápido en CPU
    cpu_threads=8,  # Ajusta según los núcleos de tu i7
    num_workers=1
)

segments, info = model.transcribe("whatsapp003.mp4", beam_size=5)

print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))