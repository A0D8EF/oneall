from django.db import models
from django.conf import settings

from django.utils import timezone

class MajorCategory(models.Model):
    name    = models.CharField(verbose_name="大カテゴリ名", max_length=20)

    def __str__(self):
        return self.name


class MinorCategory(models.Model):
    name    = models.CharField(verbose_name="小カテゴリ名", max_length=20)

    parent  = models.ForeignKey(MajorCategory, verbose_name="大カテゴリ", on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Textbook(models.Model):
    dt              = models.DateTimeField(verbose_name="投稿日時", default=timezone.now)
    user            = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="投稿者", on_delete=models.SET_NULL, null=True, blank=True)

    title           = models.CharField(verbose_name="タイトル", max_length=100)
    thumbnail       = models.ImageField(verbose_name="サムネイル画像", upload_to="textbook/thubnail/", null=True, blank=True)
    file_content    = models.FileField(verbose_name="ファイル", upload_to="textbook/movie/", null=True, blank=True)
    is_youtube      = models.BooleanField(verbose_name="Youtubeか", default=False)
    youtube_url     = models.URLField(verbose_name="YoutubeURL", null=True, blank=True)

    minor_category  = models.ForeignKey(MinorCategory, verbose_name="小カテゴリ", on_delete=models.PROTECT)

    def __str__(self):
        return self.title


