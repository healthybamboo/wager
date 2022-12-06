from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.

# ユーザー情報のモデル
class User(models.Model):
    # ユーザー名
    username = models.CharField(max_length=30,unique=True,db_index=True)
    
    # パスワード（ハッシュ化されている）
    password = models.CharField(max_length=100,db_index=True)
    
    # メールアドレス(一応とりうる最大文字数までは許容)
    email = models.EmailField(max_length=320,unique=True,db_index=True)
    
    # メール認証済みかどうか
    is_auth = models.BooleanField(default=False)
    
    # 削除フラグ
    is_delete = models.BooleanField(default=False)

    # 更新日時と作成日時は自動で設定される
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # ハッシュ化されたパスワードを登録する
    def set_password(self,password):
        self.password = make_password(password)

# タグ情報のモデル
class Tag(models.Model):
    # 所有者
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    # タグ名(100文字まで)
    name = models.CharField(max_length=100,unique=True,db_index=True)
    
    # 更新日時と作成日時は自動で設定される
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


# 収支情報のモデル
class Bed(models.Model):
    # 所有者
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    # 収支の名前
    name = models.CharField(max_length=100)
    
    # 掛けた日時
    date = models.DateField()
    
    # タグ名を選択
    tag = models.ForeignKey(Tag,on_delete=models.SET_NULL,null=True)
    
    # 賭けた金額
    spend = models.IntegerField(default=0)
    
    # 払戻し金額
    refund = models.IntegerField(default=0)
    
    # メモ
    memo = models.CharField(max_length=500,null=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

# 掛け方の情報のモデル(管理者で設定)
class BedWay(models.Model):
    # 掛け方の名前
    name = models.CharField(max_length=100,unique=True,db_index=True)
    
    # 更新日時と作成日時は自動で設定される
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

# ゲーム情報
class Game(models.Model):
    # ユーザー名
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    #　ゲーム名（100文字まで)
    name = models.CharField(max_length=100)
    
    # 掛け方
    way = models.ForeignKey(BedWay,on_delete=models.SET_NULL,null=True)
    
    # 掛け金の単位
    unit = models.IntegerField()
    
    # ゲームの状態を保持する(数列など）
    state = models.JSONField(blank=True,null=True)
    
    # ゲームが終了したかどうか（削除する場合は、レコードを削除する）
    archive = models.BooleanField(default=False)
    
    # 更新日時と作成日時は自動で設定される
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    