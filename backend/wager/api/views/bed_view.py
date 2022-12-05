from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from api.utils.auth import JWTAuthentication

from api.models import Bed,User
from api.serializers import BedSerializer
import json

import logging

logger = logging.getLogger(__name__)

# Bedクラスの基底クラス
class BedBase(APIView):
    # 認証クラスを指定
    authentication_classes = [JWTAuthentication,]
    
    # ログインしているユーザーのみアクセス可能
    permission_classes = [IsAuthenticated,]
    

# 収支一覧の処理
class BedList(BedBase):
    def get(self,request,*args,**kwargs): 
        # リクエストしたユーザーの収支一覧を取得してシリアライズ
        beds  = Bed.objects.filter(user = request.user)
        serializer = BedSerializer(beds,many=True)
        
        # レスポンスを返す
        return Response(serializer.data,status=200,headers={"ContentTypeHeader":"application/json"})
       
     # リクエストデータをシリアライズ
    def post(self,request,*args,**kwargs):
        
        # データをまとめるための辞書      
        data = dict()

        # リクエストデータが正しい確認
        serializer = BedSerializer(data= request.data)
    

        # リクエスの情報のバリデーション
        if serializer.is_valid():
            # 情報を登録
            bed = serializer.save(user=request.user)
            
            #　例外処理
            try:             
                # validation済みのユーザー情報を保存
                bed.save()
                
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

        
            
# 賭けの詳細についての処理
class BedDetail(BedBase):
    def get(self,request,*args,**kwargs):
        try : 
            # リクエストのパラメータから、idを取得し、賭けの詳細を取得
            bed = Bed.objects.get(id = kwargs['pk'])
    
            # 収支の詳細が、リクエストしたユーザーのものかを確認
            if bed.user == request.user:
                # シリアライズ
                serializer = BedSerializer(bed)
                return Response(serializer.data,status=200,headers={"ContentTypeHeader":"application/json"})
            
            # リクエストしたユーザーのものではない場合
            else:
                return Response(status=403,headers={"ContentTypeHeader":"application/json"})
        
        # 存在しない収支の詳細を取得しようとした場合
        except Bed.DoesNotExist:
            return Response(status=404,headers={"ContentTypeHeader":"application/json"})

        # TODO.例外処理を細かく追加する。
        except Exception as  e:
            return Response(status=500,headers={"ContentTypeHeader":"application/json"})
        
    def put(self,request,*args,**kwargs):
        # リクエストしたユーザーの収支一覧を取得してシリアライズ
        beds = Bed.objects.get(id = kwargs['pk'])
        serializer = BedSerializer(beds,data = request.data)
        
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
        bed = Bed.objects.get(id = kwargs['pk'])
        bed.delete()
        
        # レスポンスを返す
        return Response(status=200,headers={"ContentTypeHeader":"application/json"})
    

