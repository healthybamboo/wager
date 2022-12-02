from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.

# ユーザー情報のモデル
class User(models.Model):
    username = models.CharField(max_length=30,unique=True,db_index=True)
    password = models.CharField(max_length=100,db_index=True)
    email = models.EmailField(max_length=320,unique=True,db_index=True)
    active = models.BooleanField(default=False)

    # ハッシュ化されたパスワードを登録する
    def set_password(self,password):
        self.password = make_password(password)



# 収支情報のモデル
class Spending(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField()
    category = models.CharField(max_length=30)
    memo = models.CharField(max_length=100)
    

    
# 収支情報の詳細のモデル
class SpendingDetail(models.Model):
    money_info = models.ForeignKey(Spending,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    memo = models.CharField(max_length=100)
    amount = models.IntegerField()

     # 収支情報の詳細を登録する
    def create(self,validate_date):
        return Spending(**validate_date)

    # 収支情報の詳細を更新する
    def update(self,validate_date):
        return Spending(**validate_date)
    
    # 収支情報の詳細を削除する
    def delete(self,validate_date):
        return Spending(**validate_date)
    
    

    