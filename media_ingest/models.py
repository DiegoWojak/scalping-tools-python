from dataclasses import dataclass, field
from typing import Optional


@dataclass
class IngestResult:
    url: str
    transcript: str
    title: str = ""
    uploader: str = ""
    upload_date: str = ""
    duration_seconds: float = 0.0
    description: str = ""
    tags: list[str] = field(default_factory=list)
    language: str = ""
    error: Optional[str] = None

    @property
    def success(self) -> bool:
        return self.error is None
