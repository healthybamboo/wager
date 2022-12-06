from rest_framework import serializers
from api.models import User,Bed,BedWay ,Game


# ユーザー情報のシリアライザー
class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=320)
    password = serializers.CharField()
    
    # ユーザー情報を登録するためのシリアライザ
    def create(self,validate_date):
        return User(**validate_date)
        
# 掛け金シリアライザー
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

# ゲームのシリアライザ
class GameSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True,required=False)
    name = serializers.CharField(max_length = 100)
    way = serializers.PrimaryKeyRelatedField(queryset=BedWay.objects.all())
    unit = serializers.IntegerField()
    state = serializers.JSONField(required = False)
    archive = serializers.BooleanField(default=False,required=False)
    
    # ゲームを登録するための関数
    def create(self,validate_date):
        return Game(**validate_date)
    
    # ゲーム情報を更新するための関数
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.way = validated_data.get('way', instance.way)
        instance.unit = validated_data.get('unit', instance.unit)
        instance.state = validated_data.get('state', instance.state)
        instance.archive = validated_data.get('archive', instance.archive)
        return instance