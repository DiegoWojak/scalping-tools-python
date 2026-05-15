#!/usr/bin/env python3
"""Feed knowledge from transcriptions or reports into KNOWLEDGE.md."""

import sys
import json
from datetime import date
from pathlib import Path

KNOWLEDGE_PATH = Path(__file__).parent.parent / "references" / "KNOWLEDGE.md"
SUPPORTED_EXTENSIONS = {".txt", ".json"}


def read_source(path: Path) -> str:
    if path.suffix == ".json":
        data = json.loads(path.read_text(encoding="utf-8"))
        return json.dumps(data, ensure_ascii=False, indent=2)
    return path.read_text(encoding="utf-8")


def append_entry(source_path: Path, content: str) -> None:
    preview = content[:3000]
    truncated = "... [contenido truncado]" if len(content) > 3000 else ""
    entry = (
        f"\n\n---\n\n"
        f"## Entrada: {source_path.name} — {date.today().isoformat()}\n\n"
        f"**Fuente:** `{source_path.resolve()}`\n\n"
        f"```\n{preview}{truncated}\n```\n\n"
        f"**Patrones detectados:** _(completar manualmente o con análisis posterior)_\n"
    )
    with KNOWLEDGE_PATH.open("a", encoding="utf-8") as f:
        f.write(entry)
    print(f"Appended '{source_path.name}' to {KNOWLEDGE_PATH}")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python feed.py <file_path>")
        sys.exit(1)

    source = Path(sys.argv[1])

    if not source.exists():
        print(f"Error: file not found: {source}")
        sys.exit(1)

    if source.suffix not in SUPPORTED_EXTENSIONS:
        print(f"Error: unsupported extension '{source.suffix}'. Use .txt or .json")
        sys.exit(1)

    content = read_source(source)
    append_entry(source, content)


if __name__ == "__main__":
    main()
