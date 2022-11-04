from django.db import models
from django.conf import settings

from django.utils import timezone

class Category(models.Model):
    name    = models.CharField(verbose_name="カテゴリ名", max_length=10, unique=True)

    def __str__(self):
        return self.name

    def str_id(self):
        return str(self.id)


class News(models.Model):
    dt          = models.DateTimeField(verbose_name="投稿日時", default=timezone.now)
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="投稿者", on_delete=models.SET_NULL, null=True, blank=True)

    title       = models.CharField(verbose_name="タイトル", max_length=100)
    content     = models.CharField(verbose_name="内容", max_length=2000)

    category    = models.ForeignKey(Category, verbose_name="ニュースカテゴリ", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
