from rest_framework import serializers
from api.models import User,Spending,SpendingDetail


# ユーザー情報のシリアライザー
class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=320)
    password = serializers.CharField()
    active =  serializers.CharField(default=False)
    
    # ユーザー情報を登録するためのシリアライザ
    def create(self,validate_date):
        return User(**validate_date)
    
    # ユーザー情報を更新するためのシリアライザ
    def update(self,validate_date):
        return User(**validate_date)
        
        
# 収支のシリアライザー
class SpendingSerializer(serializers.Serializer):
    date = serializers.DateField()
    category = serializers.CharField()
    memo = serializers.CharField(max_length=100)
    user = serializers.SerializerMethodField(read_only =True)

    # 収支一覧を登録するためのシリアライザ
    def create(self,validate_date):
        return Spending(**validate_date)
    
    # 収支一覧を更新するためのシリアライザ
    def update(self,validate_date):
        return Spending(**validate_date)


# 収支詳細のシリアライザー
class SpendingDetailSerializer(serializers.Serializer):
    user = serializers.IntegerField()
    date = serializers.DateField()
    category = serializers.CharField()
    memo = serializers.CharField(max_length=100)

    def create(self,validate_date):
        return SpendingDetail(**validate_date)

        
    