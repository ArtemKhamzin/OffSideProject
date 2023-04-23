from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class BlogTag(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')

    def __str__(self):
        return self.title


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField(max_length=256, verbose_name='Название')
    short_description = models.CharField(max_length=256, verbose_name='Короткое описание')
    description = models.CharField(max_length=1024, verbose_name='Описание')
    publication_date = models.DateTimeField(verbose_name='Дата публикации')
    tags = models.ManyToManyField(BlogTag, verbose_name='Теги')
    image = models.ImageField(upload_to='blogs/', null=True, blank=True, verbose_name='Картинка')
