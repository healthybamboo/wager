from django.urls import path,include
from api.views import user_view,bed_view
from rest_framework import routers


app_name = 'api'


urlpatterns = [
    # ユーザー系
    path('user/signup/',user_view.SignUp.as_view()),
    path('user/login/',user_view.Login.as_view()),
    path('user/update',user_view.Update.as_view()),

    # 収支一覧(POST,GET)
    path('bedlist/',bed_view.BedList.as_view()),
    
    # 収支詳細(POST,GET,PUT,DELETE)
    path('bed/<int:pk>/',bed_view.BedDetail.as_view()),
     # path('spending/<int:pk>/detail/',spending_view.SpendingDetailList.as_view()),
    # path('spending/<int:pk>/detail/<int:pk2>/',spending_view.SpendingDetailDetail.as_view()),
    # path('spending/<int:pk>/detail/<int:pk2>/delete/',spending_view.SpendingDetailDetail.as_view()),
    
] 
    