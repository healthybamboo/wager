from rest_framework import serializers
from api.models import User,Bed


# ユーザー情報のシリアライザー
class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=320)
    password = serializers.CharField()
    
    # ユーザー情報を登録するためのシリアライザ
    def create(self,validate_date):
        return User(**validate_date)
    
    # ユーザー情報を更新するためのシリアライザ
    def update(self,validate_date):
        return User(**validate_date)
        
        
# 掛け金のシリアライザー
class BedSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True,required=False)
    date = serializers.DateField()
    spend = serializers.IntegerField()
    refund = serializers.IntegerField()
    memo = serializers.CharField(max_length=100)

    # 収支一覧を登録するためのシリアライザ
    def create(self,validate_date):
        return Bed(**validate_date)
    
    # 収支一覧を更新するためのシリアライザ
    def update(self,validate_date):
        return Bed(**validate_date)


        
    