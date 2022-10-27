from django.db import models
from django.conf import settings

from django.utils import timezone


class ChatGroup(models.Model):
    dt      = models.DateTimeField(verbose_name="グループ作成日", default=timezone.now)

    member  = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name="グループ内メンバー")

    def chats(self):
        return Chat.objects.filter(group=self.id).order_by("dt")

    # チャットグループをメッセージの新着順に並べる
    def latest_message(self):
        chat    = Chat.objects.filter(group=self.id).order_by("-dt").first()
        if chat:
            return chat.dt
        else:
            return self.dt
    
    def __str__(self):
        members = self.member.all()
        text    = ""
        
        for member in members:
            text    += member.handle_name + " "
        
        return text


class Chat(models.Model):
    dt      = models.DateTimeField(verbose_name="グループ作成日", default=timezone.now)
    user    = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="投稿者", on_delete=models.CASCADE)

    group   = models.ForeignKey(ChatGroup, verbose_name="所属チャットグループ", on_delete=models.CASCADE)
    message = models.CharField(verbose_name="メッセージ", max_length=20000)
