from django.db import models
from django.utils import timezone
from django.conf import settings
from social_django import models as social

# 選択肢にない値を保存しようとしたらエラーにするだけで良いのですから、
CLAN_AUTHORITY = (
    (1, 'Master'),
    (2, 'Sub Master'),
    (3, 'Member')
)


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=255)
    tag = models.CharField(max_length=5)
    agenda = models.CharField(max_length=255)
    # upload_toで指定するパスは内部的にMEDIA_ROOTと結合される
    # clan_image = models.ImageField(upload_to='app1')

    def __str__(self):
        return self.name


class Player(models.Model):
    # twitter認証DBとの紐づけ
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    # 登録日
    registered_date = models.DateTimeField(default=timezone.now)
    # フォームでの入力は任意、データベースにはnullが保存される
    psn_id = models.CharField(blank=True, null=False, max_length=30)
    # 所属しているクラン
    belong_clan = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    # クラン内での権利 1:クランマスター 2:副マスター 3:メンバー
    belong_clan_authority = models.IntegerField(choices=CLAN_AUTHORITY, default=1)

    #def __str__(self):
       #return self.u

