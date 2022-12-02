from django.urls import path,include
from api.views import user_view,spending_view
from rest_framework import routers


app_name = 'api'


urlpatterns = [
    # ユーザー系
    path('user/signup/',user_view.SignUp.as_view()),
    path('user/login/',user_view.Login.as_view()),
    path('user/update',user_view.Update.as_view()),

    # 収支一覧(POST,GET)
    path('spending/',spending_view.SpendingList.as_view()),
    
    # 収支詳細(POST,GET,PUT,DELETE)
    # path('spending/<int:pk>/',spending_view.SpendingDetail.as_view()),
    
    # 
    # path('spending/<int:pk>/detail/',spending_view.SpendingDetailList.as_view()),
    # path('spending/<int:pk>/detail/<int:pk2>/',spending_view.SpendingDetailDetail.as_view()),
    # path('spending/<int:pk>/detail/<int:pk2>/delete/',spending_view.SpendingDetailDetail.as_view()),
    
] 
    