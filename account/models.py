from django.db import models
from datetime import datetime

# Create your models here.

class User(models.Model):
    """
    ユーザ
    """    
    class Meta:
        # テーブル名定義
        db_table = 'users'

    name = models.CharField(verbose_name='ユーザー名', max_length=255)
    profile_image = models.CharField(verbose_name='プロファイル画像', max_length=255,null=True, blank=True)
    email = models.CharField(verbose_name='メールアドレス', max_length=255, unique=True)
    password = models.CharField(verbose_name='パスワード', max_length=255)
    # created_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True) # 登録時1回だけ自動入力
    created_at = models.DateTimeField(verbose_name='登録日時', default=datetime.now)
    updated_at =  models.DateTimeField(verbose_name='更新日時', auto_now=True) # 更新時毎回自動入力

    # 管理サイト用表示文字列
    def __str__(self):
        return self.name


