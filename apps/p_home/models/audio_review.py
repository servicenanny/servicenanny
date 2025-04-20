from django.db import models


class AudioReview(models.Model):
    number = models.SmallIntegerField(verbose_name='Порядковый номер', help_text='Номер, по которому определяется порядок отзыва в блоке с отзывами')
    from_client = models.CharField(max_length=255, verbose_name="Информация о клиенте, который написал отзыв", help_text="Отображается сверху блока. Максимум 255 символа")
    text = models.CharField(max_length=2047, verbose_name="Отзыв", help_text="Основной текст блока. Максимум 2047 символов", null=True)
    preview = models.ImageField(upload_to='reviews/img', verbose_name="Загрузить превью к аудиоотзыву")
    file = models.FileField(upload_to='reviews/audio', verbose_name="Аудио", help_text="Загрузите аудио с отзывом клиента")

    def __repr__(self):
        return str(self.from_client)
    
    def __str__(self):
        return str(self.from_client)

    class Meta:
        verbose_name = 'Аудиоотзыв'
        verbose_name_plural = 'Аудиоотзывы'