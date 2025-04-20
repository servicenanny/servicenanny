from dataclasses import dataclass


@dataclass
class ReviewDTO:
    number: int
    from_client: str
    preview_url: str | None
    text: str
    file_url: str
    is_video: bool = False
    is_audio: bool = False
    