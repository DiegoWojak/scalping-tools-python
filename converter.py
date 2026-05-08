from faster_whisper import WhisperModel

# Configuración optimizada para CPU
print("🔄 Iniciando transcripción...")
model = WhisperModel("base", device="cpu", compute_type="int8")

# Transcribir el video
print("🎙️ Procesando audio...")
name = "whatsapp001.mp4"
segments, info = model.transcribe(name, language="es")

# Mostrar y guardar resultados
print(f"\n📊 Idioma detectado: {info.language} (probabilidad: {info.language_probability:.2%})")
print("\n" + "="*60)
print("📝 TRANSCRIPCIÓN:")
print("="*60)

# Lista para guardar todo el texto
texto_completo = []

# Procesar cada segmento
for segment in segments:
    # Guardar en lista
    texto_completo.append(segment.text)
    
    # Mostrar en pantalla
    print(f"[{segment.start:>7.2f}s → {segment.end:>7.2f}s] {segment.text}")

print("="*60)

# Guardar en archivo TXT
with open(f"{name}_transcripcion.txt", "w", encoding="utf-8") as archivo:
    # Opción 1: Guardar con marcas de tiempo
    archivo.write("="*60 + "\n")
    archivo.write("TRANSCRIPCIÓN DE VIDEO\n")
    archivo.write("="*60 + "\n\n")
    
    for segment in segments:
        archivo.write(f"[{segment.start:.2f}s → {segment.end:.2f}s] {segment.text}\n")
    
    # Opción 2: Guardar solo el texto plano (sin tiempos)
    archivo.write("\n" + "="*60 + "\n")
    archivo.write("TEXTO COMPLETO:\n")
    archivo.write("="*60 + "\n\n")
    archivo.write(" ".join(texto_completo))

print(f"\n✅ Transcripción guardada en '{name}_transcripcion.txt'")
print(f"📄 Archivo creado en: D:/Python Workspace/VideoToText/transcripcion.txt")