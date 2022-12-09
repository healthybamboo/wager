from django.urls import path,include
from api.views import user_view,bed_view,game_view,csrf_view
from rest_framework import routers


app_name = 'api'


urlpatterns = [
    # セキュリティ
    path('csrf/',csrf_view.csrf_view),
    
    # ユーザー
    path('user/signup/',user_view.SignUp.as_view()),
    path('user/login/',user_view.Login.as_view()),
    path('user/update/',user_view.Update.as_view()),

    # 収支
    path('beds/',bed_view.BedList.as_view()),
    path('beds/<int:pk>/',bed_view.BedDetail.as_view()),

    # ゲーム
    path('games/',game_view.GameList.as_view()),
    path('games/<int:pk>/',game_view.GameDetail.as_view()),
] 
    