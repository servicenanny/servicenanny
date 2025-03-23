from django.db import models


class VideoReview(models.Model):
    number = models.SmallIntegerField(verbose_name='Порядковый номер', help_text='Номер, по которому определяется порядок отзыва в блоке с отзывами')
    from_client = models.CharField(max_length=255, verbose_name="Информация о клиенте, который написал отзыв", help_text="Отображается сверху блока. Максимум 255 символа")
    preview = models.ImageField(upload_to='reviews/img', verbose_name="Вы можете добавить превью к видеоотзыву", null=True)
    file = models.FileField(upload_to='reviews/video', verbose_name="Видео", help_text="Загрузите видео с отзывом клиента")

    def __repr__(self):
        return str(self.from_client)
    
    def __str__(self):
        return str(self.from_client)

    class Meta:
        verbose_name = 'Видеоотзыв'
        verbose_name_plural = 'Видеоотзывы'