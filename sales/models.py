from django.db import models
from django.conf import settings

from django.utils import timezone

class AC(models.Model):
    dt      = models.DateTimeField(verbose_name="投稿日時", default=timezone.now)
    user    = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="投稿者", on_delete=models.CASCADE)

    ac_date = models.DateTimeField(verbose_name="AC日時")
    c_name  = models.CharField(verbose_name="Cさんの名前", max_length=10, null=True, blank=True)
    place   = models.CharField(verbose_name="AC場所", max_length=200, null=True, blank=True)

    c_is_ac_active = models.BooleanField(verbose_name="ACステータス", default=True)

    def __str__(self):
        return self.c_name

    def str_id(self):
        return str(self.id)


class Question(models.Model):
    dt      = models.DateTimeField(verbose_name="投稿日時", default=timezone.now)
    user    = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="投稿者", on_delete=models.CASCADE)

    q_date  = models.DateField(verbose_name="質問日")
    ac      = models.ForeignKey(AC, verbose_name="対応するAC", on_delete=models.CASCADE)

    c_is_question_active    = models.BooleanField(verbose_name="質問ステータス", default=True)

    def __str__(self):
        return self.ac.c_name


class ABC(models.Model):
    dt          = models.DateTimeField(verbose_name="投稿日時", default=timezone.now)
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="投稿者", on_delete=models.CASCADE)

    abc_date    = models.DateTimeField(verbose_name="ABC日時")
    question    = models.ForeignKey(Question, verbose_name="対応する質問", on_delete=models.CASCADE)

    c_is_abc_active = models.BooleanField(verbose_name="ABCステータス", default=True)

    def __str__(self):
        return self.question.ac.c_name


class Interview(models.Model):
    dt              = models.DateTimeField(verbose_name="投稿日時", default=timezone.now)
    user            = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="投稿者", on_delete=models.CASCADE)

    interview_date  = models.DateTimeField(verbose_name="面談日時")
    abc             = models.ForeignKey(ABC, verbose_name="対応するABC", on_delete=models.CASCADE)

    c_is_interview_active    = models.BooleanField(verbose_name="面談ステータス", default=True)

    def __str__(self):
        return self.abc.question.ac.c_name


class Contract(models.Model):
    dt              = models.DateTimeField(verbose_name="投稿日時", default=timezone.now)
    user            = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="投稿者", on_delete=models.CASCADE)

    contract_date   = models.DateField(verbose_name="契約日時")
    interview       = models.ForeignKey(Interview, verbose_name="対応する面談", on_delete=models.CASCADE)

    def __str__(self):
        return self.interview.abc.question.ac.c_name



