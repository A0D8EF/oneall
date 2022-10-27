from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings

from django.utils import timezone

class Tag(models.Model):
    name    = models.CharField(verbose_name="タグ名", max_length=10)

    def __str__(self):
        return self.name

    def str_id(self):
        return str(self.id)
    

class Question(models.Model):
    dt      = models.DateTimeField(verbose_name="投稿日時", default=timezone.now)
    user    = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="投稿者", on_delete=models.CASCADE)

    title   = models.CharField(verbose_name="タイトル", max_length=100)
    content = models.CharField(verbose_name="内容", max_length=2000)

    tag     = models.ManyToManyField(Tag, related_name="question_tag", verbose_name="タグ", blank=True)
    good    = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="question_good", verbose_name="いいねしたユーザー", blank=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    dt      = models.DateTimeField(verbose_name="投稿日時", default=timezone.now)
    user    = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="投稿者", on_delete=models.CASCADE)

    target  = models.ForeignKey(Question, verbose_name="質問", on_delete=models.CASCADE)
    content = models.CharField(verbose_name="内容", max_length=2000)

    good    = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="answer_good", verbose_name="いいねしたユーザー", blank=True)

