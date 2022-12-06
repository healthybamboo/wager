from rest_framework import serializers
from api.models import User,Bed,BedWay,Game,Tag


# ユーザー情報のシリアライザー
class UserSerializer(serializers.Serializer):
    #　ユーザー名
    username = serializers.CharField(max_length=30)
    # メール
    email = serializers.EmailField(max_length=320)
    # パスワード
    password = serializers.CharField()
    
    # ユーザー情報を登録するためのシリアライザ
    def create(self,validate_date):
        return User(**validate_date)
        
# 掛け金シリアライザー
class BedSerializer(serializers.Serializer):
    # PK
    id = serializers.IntegerField(read_only=True,required=False)
    #　名前（有馬記念,凱旋門賞など）
    name = serializers.CharField(max_length=100)
    # タグ（競馬,競艇,パチンコ,...)
    tag = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(),required=False)
    # 日付
    date = serializers.DateField()
    # 賭け金
    spend = serializers.IntegerField()
    # 払戻金
    refund = serializers.IntegerField()
    # 掛け金のメモ
    memo = serializers.CharField(max_length=100)

    # 収支一覧を登録するためのシリアライザ
    def create(self,validate_date):
        return Bed(**validate_date)
    
    # 収支一覧を更新するためのシリアライザ
    def update(self,instance,validate_date):
        instance.name = validate_date.get('name',instance.name)
        instance.tag = validate_date.get('tag',instance.tag)
        instance.date = validate_date.get('date',instance.date)
        instance.spend = validate_date.get('spend',instance.spend)
        instance.refund = validate_date.get('refund',instance.refund)
        instance.memo = validate_date.get('memo',instance.memo)
        return instance

# ゲームのシリアライザ
class GameSerializer(serializers.Serializer):
    # PK
    id = serializers.IntegerField(read_only=True,required=False)
    # ゲーム名(5月の地方競馬など)
    name = serializers.CharField(max_length = 100)
    # FK 賭けるシステム（Monte Carlo法、Cocomo法など）
    way = serializers.PrimaryKeyRelatedField(queryset=BedWay.objects.all())
    # 賭ける単位（100円,1000円,10000円など）
    unit = serializers.IntegerField()
    # ゲームの状態を保つ（状態を保持する）
    state = serializers.JSONField(required = False)
    # アーカイブ（ゲームを終了する場合はTrue）
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