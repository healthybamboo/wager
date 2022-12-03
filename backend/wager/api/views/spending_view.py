from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from api.utils.auth import JWTAuthentication

from api.models import Spending,User
from api.serializers import SpendingSerializer,SpendingDetailSerializer
import json

import logging

logger = logging.getLogger(__name__)

# Spendingクラスの基底クラス
class SpendingBase(APIView):
    # 認証クラスを指定
    authentication_classes = [JWTAuthentication,]
    
    # ログインしているユーザーのみアクセス可能
    permission_classes = [IsAuthenticated,]
    

# 収支一覧の処理
class SpendingList(SpendingBase):
    def get(self,request,*args,**kwargs): 
        # リクエストしたユーザーの収支一覧を取得してシリアライズ
        spendings  = Spending.objects.filter(user = request.user)
        serializer = SpendingSerializer(spendings,many=True)
        
        # レスポンスを返す
        return Response(serializer.data,status=200,headers={"ContentTypeHeader":"application/json"})
       
     # リクエストデータをシリアライズ
    def post(self,request,*args,**kwargs):
        
        # データをまとめるための辞書      
        data = dict()

        # リクエストデータが正しい確認
        serializer = SpendingSerializer(data= request.data)
    

        # リクエスの情報のバリデーション
        if serializer.is_valid():
            # 情報を登録
            spending = serializer.save(user=request.user)
            
            #　例外処理
            try:             
                # validation済みのユーザー情報を保存
                spending.save()
                
                # 正常に登録できた場合
                return Response(serializer.data, status=201,headers={"ContentTypeHeader":"application/json"})

            # TODO...例外処理を細かく追加する。
            # フォームの内容は間違いないが、登録に失敗した場合
            except Exception as e:
                logger.debug(msg=str(e))
                return Response(status=409,headers={"ContentTypeHeader":"application/json"})

        else:
            # フォームの内容に問題があった場合はエラーを返す
            return Response(serializer.errors, status=409,headers={"ContentTypeHeader":"application/json"})

        
            
# 収支の詳細の処理
class SpendingDetail(SpendingBase):
    def get(self,request,*args,**kwargs):
        # リクエストしたユーザーの収支一覧を取得してシリアライズ
        try : 
            spending = Spending.objects.get(id = kwargs['pk'])
            
            # 収支の詳細が、リクエストしたユーザーのものかを確認
            if spending.user == request.user:
                serializer = SpendingSerializer(spending)
                return Response(serializer.data,status=200,headers={"ContentTypeHeader":"application/json"})
            
            # リクエストしたユーザーのものではない場合
            else:
                return Response(status=403,headers={"ContentTypeHeader":"application/json"})
        
        # 存在しない収支の詳細を取得しようとした場合
        except Spending.DoesNotExist:
            return Response(status=404,headers={"ContentTypeHeader":"application/json"})

        # TODO.例外処理を細かく追加する。
        except Exception as  e:
            return Response(status=500,headers={"ContentTypeHeader":"application/json"})
        
    def put(self,request,*args,**kwargs):
        # リクエストしたユーザーの収支一覧を取得してシリアライズ
        spending = Spending.objects.get(id = kwargs['pk'])
        serializer = SpendingSerializer(spending,data = request.data)
        
        # リクエスの情報のバリデーション
        if serializer.is_valid():
            # 情報を登録
            spending = serializer.save(user=request.user)
            
            #　例外処理
            try:             
                # validation済みのユーザー情報を保存
                spending.save()
                
                # 正常に登録できた場合
                return Response(serializer.data, status=201,headers={"ContentTypeHeader":"application/json"})

            # TODO...例外処理を細かく追加する。
            # フォームの内容は間違いないが、登録に失敗した場合
            except Exception as e:
                logger.debug(msg=str(e))
                return Response(status=409,headers={"ContentTypeHeader":"application/json"})

        else:
            # フォームの内容に問題があった場合はエラーを返す
            return Response(serializer.errors, status=409,headers={"ContentTypeHeader":"application/json"})
        
    def delete(self,request,*args,**kwargs):
        # リクエストしたユーザーの収支一覧を取得してシリアライズ
        spending = Spending.objects.get(id = kwargs['pk'])
        spending.delete()
        
        # レスポンスを返す
        return Response(status=200,headers={"ContentTypeHeader":"application/json"})
    

# 収支の詳細の一覧の処理
class SpendingDetailList(SpendingBase):
    pass

# 収支の詳細の詳細の処理
class SpendingDetailDetail(SpendingBase):
    pass
