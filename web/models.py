from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class BlogTag(models.Model):
    title = models.CharField(max_length=256)


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    short_description = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)
    publication_date = models.DateTimeField()
    tags = models.ManyToManyField(BlogTag)
    image = models.ImageField(upload_to='blogs/', null=True, blank=True)
