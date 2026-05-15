import json
import subprocess
import tempfile
import uuid
from pathlib import Path
from urllib.parse import urlparse

from faster_whisper import WhisperModel

from .models import IngestResult

_WHISPER_MODEL: WhisperModel | None = None
_TEMP_DIR = Path(tempfile.gettempdir()) / "media_ingest"
_MAX_WAV_MB = 150


def _get_model() -> WhisperModel:
    global _WHISPER_MODEL
    if _WHISPER_MODEL is None:
        _WHISPER_MODEL = WhisperModel("base", device="cpu", compute_type="int8")
    return _WHISPER_MODEL


def _validate_url(url: str) -> None:
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        raise ValueError(f"URL inválida: {url!r}")


def _fetch_metadata(url: str) -> dict:
    result = subprocess.run(
        ["yt-dlp", "--dump-json", "--no-playlist", url],
        capture_output=True,
        text=True,
        check=True,
    )
    return json.loads(result.stdout)


def _download_audio(url: str, out_dir: Path) -> Path:
    stem = str(uuid.uuid4())
    wav_out = out_dir / f"{stem}.wav"

    subprocess.run(
        [
            "yt-dlp",
            "--no-playlist",
            "-x",
            "--audio-format", "wav",
            "--postprocessor-args", "ffmpeg:-ar 16000 -ac 1",
            "-o", str(wav_out),
            url,
        ],
        capture_output=True,
        check=True,
    )

    if wav_out.exists() and wav_out.stat().st_size / (1024 * 1024) > _MAX_WAV_MB:
        mp3_out = out_dir / f"{stem}.mp3"
        subprocess.run(
            [
                "yt-dlp",
                "--no-playlist",
                "-x",
                "--audio-format", "mp3",
                "-o", str(mp3_out),
                url,
            ],
            capture_output=True,
            check=True,
        )
        wav_out.unlink(missing_ok=True)
        return mp3_out

    return wav_out


def _transcribe(audio_path: Path) -> tuple[str, str]:
    model = _get_model()
    segments, info = model.transcribe(str(audio_path), language=None)
    text = " ".join(seg.text.strip() for seg in segments)
    return text, info.language


def ingest(url: str) -> IngestResult:
    try:
        _validate_url(url)
    except ValueError as exc:
        return IngestResult(url=url, transcript="", error=str(exc))

    _TEMP_DIR.mkdir(parents=True, exist_ok=True)
    audio_path: Path | None = None

    try:
        meta = _fetch_metadata(url)
        audio_path = _download_audio(url, _TEMP_DIR)
        transcript, language = _transcribe(audio_path)

        return IngestResult(
            url=url,
            transcript=transcript,
            title=meta.get("title", ""),
            uploader=meta.get("uploader", ""),
            upload_date=meta.get("upload_date", ""),
            duration_seconds=float(meta.get("duration", 0) or 0),
            description=meta.get("description", ""),
            tags=list(meta.get("tags") or []),
            language=language,
        )
    except subprocess.CalledProcessError as exc:
        stderr = exc.stderr or ""
        return IngestResult(url=url, transcript="", error=f"yt-dlp error: {stderr[:300]}")
    except Exception as exc:
        return IngestResult(url=url, transcript="", error=str(exc))
    finally:
        if audio_path and audio_path.exists():
            audio_path.unlink(missing_ok=True)
