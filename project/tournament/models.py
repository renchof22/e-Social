from django.db import models
from django.contrib.auth.models import User
from app1 import models as APP1


# 大会を表現するモデル
class Tournament(models.Model):
    # 大会名
    name = models.CharField(max_length=30, unique=True)
    # 大会詳細
    description = models.CharField(max_length=100)
    # 開催者　Userに紐づけ
    organizer = models.ForeignKey(User, related_name='tournaments', on_delete=models.CASCADE)
    # 参加可能チーム数
    num = models.IntegerField(max_length=20)


# 大会に参加するチームモデル　Tournamentモデルに属する
class Participant(models.Model):
    # 参加チーム
    team = models.ForeignKey(APP1.Team, related_name='participants', on_delete=models.PROTECT)
    # 参加日時
    time = models.DateTimeField(auto_now_add=True)
    # ひとこと
    message = models.TextField(max_length=4000)
