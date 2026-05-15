"""
CLI entry point: python -m media_ingest.feed_url <url>
Prints transcript + metadata as plain text — ready to pipe into /feed.
"""
import sys

from .ingest import ingest


def main() -> None:
    if len(sys.argv) < 2:
        print("Uso: python -m media_ingest.feed_url <url>", file=sys.stderr)
        sys.exit(1)

    url = sys.argv[1]
    result = ingest(url)

    if not result.success:
        print(f"ERROR: {result.error}", file=sys.stderr)
        sys.exit(1)

    print(f"TITLE: {result.title}")
    print(f"UPLOADER: {result.uploader}")
    print(f"DATE: {result.upload_date}")
    print(f"DURATION: {result.duration_seconds:.0f}s")
    print(f"LANGUAGE: {result.language}")
    if result.tags:
        print(f"TAGS: {', '.join(result.tags[:10])}")
    print()
    print("--- TRANSCRIPT ---")
    print(result.transcript)


if __name__ == "__main__":
    main()
