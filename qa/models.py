from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

class Tag(models.Model):
    name    = models.CharField(verbose_name="タグ名", max_length=10)

    def __str__(self):
        return self.name

    def str_id(self):
        return str(self.id)
    

class Question(models.Model):

    title   = models.CharField(verbose_name="タイトル", max_length=100)
    content = models.CharField(verbose_name="内容", max_length=2000)

    dt      = models.DateTimeField(verbose_name="投稿日時", default=timezone.now)
    user    = models.ForeignKey(User, verbose_name="投稿者", on_delete=models.CASCADE)

    tag     = models.ManyToManyField(Tag, related_name="question_tag", verbose_name="タグ")
    good    = models.ManyToManyField(User, related_name="question_good", verbose_name="いいねしたユーザー")

    def __str__(self):
        return self.title
