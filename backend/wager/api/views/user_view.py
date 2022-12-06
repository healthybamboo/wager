from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import UserSerializer
from api.utils.auth import NormalAuthentication
import logging

from api.models import User
logger = logging.getLogger(__name__)

# Create your views here.

# ユーザー登録処理
class SignUp(APIView):
    def post(self,request):
        # ユーザー情報をシリアライズ
        serializer = UserSerializer(data=request.data)
        
        # ユーザー情報のバリデーション
        if serializer.is_valid():
            # ユーザー情報を登録
            user = serializer.save()
            user.set_password(serializer.data.get("password"))
            
            #　例外処理
            try:             
                # validation済みのユーザー情報を保存
                user.save()
                
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


# ユーザー更新処理
class Update(APIView):
    def put(self,request):
        # TODO.　ユーザー情報の更新処理を追加する。
        return Response(status=404)
        
# ログイン処理
class Login(APIView):

    authentication_classes = [NormalAuthentication,]

    def post(self,request,*args,**kwargs):
        return Response(data={"token":request.user},status=200)
    
    


