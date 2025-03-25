from dataclasses import dataclass


@dataclass
class ReviewDTO:
    number: int
    from_client: str
    text: str
    preview_url: str | None
    file_url: str
    is_video: bool = False
    is_audio: bool = False
    