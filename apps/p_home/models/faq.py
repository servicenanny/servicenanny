from django.db import models


class FAQ(models.Model):
    question = models.CharField(max_length=1023, verbose_name="Вопрос", help_text="Отображается сверху блока. Максимум 1023 символа")
    answer = models.CharField(max_length=2047, verbose_name="Ответ", help_text="Основной текст блока. Максимум 2047 символов")

    def __repr__(self):
        return str(self.question)
    
    def __str__(self):
        return str(self.question)

    class Meta:
        verbose_name = 'Часто задаваемый вопрос'
        verbose_name_plural = 'Часто задаваемые вопросы'