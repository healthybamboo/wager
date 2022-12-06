from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from api.utils.auth import JWTAuthentication

from api.models import Bed,Game
from api.serializers import GameSerializer

import json 
import logging

logger = logging.getLogger(__name__)

class GameBase(APIView):
    # 認証クラスを指定
    authentication_classes = [JWTAuthentication,]
    
    # ログインしているユーザーのみアクセス可能
    permission_classes = [IsAuthenticated,]
    
class GameList(GameBase):
    def get(self,request, *args, **kwargs):
        # 接続ユーザーの取得
        user = request.user
        
        # ゲーム一覧を取得
        games = Game.objects.filter(user=user)
        
        # シリアライザー
        serializer = GameSerializer(games,many=True)
        
        # 正常な値を返す
        return Response(status=200,data=json.dumps(serializer.data) ,headers={"ContentTypeHeader":"application/json"})
    
    def post(self,request,*args,**kwargs):
         # 接続ユーザーの取得
        user = request.user
        
        # ゲームオブジェクトを作成
        serializer = GameSerializer(data=request.data)
        
        # リクエストのバリデーション
        if serializer.is_valid():
            game = serializer.save(user= request.user)
              
            #　例外処理
            try:             
                # validation済みのユーザー情報を保存
                game.save()
                
                # 正常に登録できた場合
                return Response(serializer.data, status=201,headers={"ContentTypeHeader":"application/json"})

            # TODO...例外処理を細かく追加する。
            # フォームの内容は間違いないが、登録に失敗した場合
            except Exception as e:
                logger.debug(msg=str(e))
                return Response(status=409,headers={"ContentTypeHeader":"application/json"})
    
        else:
            return Response(status=409,data= serializer.errors)
           
    
class GameDetail(GameBase):
    def put(self,request,*args,**kwargs):
        # 例外処理
        try :
            # IDに紐づくゲームを取得
            game = Game.objects.get(id=kwargs['pk'])

            # ユーザーが一致しているか確認
            if request.user == game.user:

                # シリアライザー
                serializer = GameSerializer(game,data=request.data,partial=True)
                
                # リクエストのバリデーション
                if serializer.is_valid():
                    # シリアライザーの保存
                    game = serializer.save()
                    
                    # データベースに保存
                    game.save()
                    return Response(status=200,data=serializer.data)
                else:
                    return Response(status=409)
            else:
                return Response(status=403)
        
        # 指定されたIDのゲームが存在しない場合
        except Game.DoesNotExist:
            return Response(status=404)

        # TODO...例外処理を細かく追加する。
        except Exception as e:
            return Response(status=500)
        
    def get(self,request, *args, **kwargs):
        try : 
            # IDに紐づくゲームを取得
            game = Game.objects.get(id=kwargs['pk'])
            
            # ユーザーが一致するか確認
            if request.user == game.user:
                
                # 値を返す
                return Response(status=200,data=GameSerializer(game).data)
            
            # 一致しない場合は403エラーを返す
            else:
                return Response(status=403)

        except Game.DoesNotExist:
            return Response(status=404)

        # TODO...例外処理を細かく追加する。
        except Exception as e:
            return Response(status=500)
    
    # 削除処理
    def delete(self,request,*args,**kwargs):
        # TODO...メッセージを返すようにする
        try : 
            # IDに紐づくゲームを取得
            game = Game.objects.get(id=kwargs['pk'])

            # ユーザーが一致するか確認
            if request.user == game.user:
                # 削除
                game.delete()
                return Response(status=200)
            else:
                return Response(status=403)
        except Game.DoesNotExist:
            return Response(status=404)

        # TODO...例外処理を細かく追加する。
        except Exception as e:
            return Response(status=500)


    
