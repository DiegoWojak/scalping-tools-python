# VideoToText — Transcriptor de Video a Texto

Herramienta para transcribir el audio de videos MP4 a texto usando [faster-whisper](https://github.com/SYSTRAN/faster-whisper). Procesa el video localmente en CPU, detecta el idioma automáticamente y genera un archivo `.txt` con marcas de tiempo y texto plano.

---

## Requisitos

- Python 3.8+
- [ffmpeg](https://ffmpeg.org/) instalado y disponible en el PATH

---

## Instalación

1. (Recomendable) Crea un entorno virtual:

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

---

## USO

1. Coloca el archivo de video (`.mp4`) en la carpeta del proyecto.
2. Edita la variable `name` en `converter.py` con el nombre de tu archivo:

```python
name = "tu_video.mp4"
```

3. Ejecuta el script:

```bash
python converter.py
```

---

## Salida

El script genera un archivo `<nombre_video>.mp4_transcripcion.txt` con dos secciones:

- **Segmentos con marcas de tiempo** — cada fragmento de audio con inicio y fin en segundos.
- **Texto completo** — la transcripción unida en un solo bloque de texto plano.

Ejemplo de salida en consola:

```
📊 Idioma detectado: es (probabilidad: 99.39%)
============================================================
📝 TRANSCRIPCIÓN:
============================================================
[   0.00s →    9.68s]  lo que vamos a hacer en tu caso es...
[   9.68s →   17.24s]  evaluación, tu asesoría, negociación...
============================================================
✅ Transcripción guardada en 'tu_video.mp4_transcripcion.txt'
```

---

## Dependencias

| Paquete | Versión |
|---|---|
| faster-whisper | 1.2.1 |

> El modelo utilizado es `base` con cómputo `int8` optimizado para CPU. Para mayor precisión puedes cambiar a `small`, `medium` o `large` en `converter.py`.
