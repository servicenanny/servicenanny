from typing import Iterable

from apps.p_home.models import VideoReview, AudioReview
from .dto.review import ReviewDTO


class ReviewsView:
    def get(self) -> Iterable[ReviewDTO]:
        reviews: list[ReviewDTO] = []
        self.__set_audio_reviews(reviews)
        self.__set_video_reviews(reviews)
        self.__order_by_number(reviews)
        return reviews
        
    def __set_video_reviews(self, reviews: list[ReviewDTO]) -> None:
        for review in VideoReview.objects.all():
            dto = ReviewDTO(
                number = review.number,
                from_client = review.from_client,
                text = review.text,
                preview_url = review.preview.url,
                file_url = review.file.url,
                is_video = True
            )
            reviews.append(dto)

    def __set_audio_reviews(self, reviews: list[ReviewDTO]) -> None:
        for review in AudioReview.objects.all():
            dto = ReviewDTO(
                number = review.number,
                from_client = review.from_client,
                preview_url = review.preview.url,
                file_url = review.file.url,
                is_audio = True
            )
            reviews.append(dto)

    def __order_by_number(self, reviews: list[ReviewDTO]) -> None:
        reviews.sort(key=lambda x: x.number, reverse=False)