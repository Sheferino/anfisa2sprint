from django.db import models


class PublishedModel(models.Model):
    """Абстрактная модель. Добвляет флаг is_published."""
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    title = models.CharField(max_length=256, verbose_name='Название', help_text='Уникальное название, не более 256 символов')

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.title
