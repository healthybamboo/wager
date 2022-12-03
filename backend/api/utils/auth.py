import time
import jwt
from wager.settings import SECRET_KEY
from django.contrib.auth.hashers import check_password
from rest_framework.authentication import BaseAuthentication,get_authorization_header
from rest_framework import exceptions
from api.models import User


# ログイン認証クラス
class NormalAuthentication(BaseAuthentication):
    # JSON Web Tokenを生成するための関数
    @staticmethod
    def generate_jwt(user):
        # JWTの有効期限を設定
        timestamp = int(time.time()) + 60*60*24*7
                
        token = jwt.encode(
            payload=
                {
                    "userid":user.pk,
                    "username":user.username,
                    "exp":timestamp
                },

            key=SECRET_KEY,
        )

        return token

    # 認証を行うための関数
    def authenticate(self, request):
        
        # リクエストボディからユーザー名とパスワードを取得 
        username = request._request.POST.get("username")
        password = request._request.POST.get("password")
        
        
        # ユーザー名が一致するユーザーを取得
        user_obj = User.objects.filter(username=username).first()  
         
        
        # ユーザの取得に失敗した場合
        if not user_obj:
            raise exceptions.AuthenticationFailed("認証に失敗しました") 
        
        # パスワードが一致しない場合
        elif not check_password(password,user_obj.password):
            raise exceptions.AuthenticationFailed("パスワードが違います")
        
        # tokenを生成して返す
        token = self.generate_jwt(user_obj)
        
        return (token,None)
    

        def  authenticate_header(self, request):
             pass            

# JWT認証クラス
class JWTAuthentication(BaseAuthentication):
    keyword = 'JWT'
    model = None
    
    def authenticate_header(self,request):
        pass
    
    # 認証を行うための関数
    def authenticate(self, request):
        
        # ヘッダーからTokenを取得
        header = get_authorization_header(request)
        
        # Tokenが取得できなかった場合    
        if not header:
            return None
        
        auth = header.split()

        
        # 　認証情報が不正な場合
        if  auth[0].lower() != self.keyword.lower().encode():
            return None
        
        
        if len(auth) == 1:
            msg = "Authorization 無効"
            raise exceptions.AuthenticationFailed(msg)
        
        elif len(auth) > 2 :
            msg = "Authorization 無効　スペースはない"
            raise exceptions.AuthenticationFailed(msg)
        
        try:
            # トークンを取得
            jwt_token = auth[1]
            jwt_info = jwt.decode(jwt=jwt_token,key=SECRET_KEY,algorithms="HS256")
            
            # TokenからユーザーIDを取得
            userid = jwt_info.get("userid")
            
            try:
                # ユーザーを取得し、認証済みを返す
                user=User.objects.get(pk=userid)
                user.is_authenticated = True
                return (user,jwt_token)
            except:
                msg = "ユーザーが見つかりません"
                raise exceptions.AuthenticationFailed(msg)
            
        except jwt.ExpiredSignatureError:
            msg = "tokenはタイムアウトしています"
            raise exceptions.AuthenticationFailed(msg)
                                

        