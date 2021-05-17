from django.db import models


class Quote(models.Model):
    text = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to='',
        blank=True,
        null=True,
        verbose_name="Изображение публикации"
        )
