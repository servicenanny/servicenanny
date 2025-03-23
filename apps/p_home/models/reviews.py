from django.db import models


class Review(models.Model):
    from_client = models.CharField(max_length=255, verbose_name="Информация о клиенте, который написал отзыв", help_text="Отображается сверху блока. Максимум 255 символа")
    text = models.CharField(max_length=2047, verbose_name="Отзыв", help_text="Основной текст блока. Максимум 2047 символов")

    def __repr__(self):
        return str(self.from_client)
    
    def __str__(self):
        return str(self.from_client)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'