import os
import pytest
import ast
from django.test import client
from django.core.management import  call_command

from api.models import Spending



#  収支一覧ページのテスト
class Test_Spending_List_Page:
    PATH = '/api/spendinglist/'
    
    # ログイン処理
    @staticmethod
    def login():
        c = client.Client()
        data = {
            "username": "MrPython",
            "password": "password1234", 
         }
        token = ast.literal_eval(c.post(path= '/api/user/login/',data=data).content.decode('utf-8'))['token']
        
        return token
        
    # データの登録
    @pytest.fixture(autouse=True, scope='class')
    def setUp(self, django_db_setup, django_db_blocker):
        with django_db_blocker.unblock():
                 # # fixturesからデータを読んでDBに入れる
                call_command('loaddata', 'tests/fixtures/users.json')
    
    # ログインせず収支一覧ページにアクセスした場合、閲覧禁止エラーが返却されることを確認するテスト
    def test_bad_user_acces_denied(self):
        c = client.Client()
        response = c.get(self.PATH)

        assert response.status_code == 403
        
    # ログインした状態で収支一覧ページにアクセスした場合、正常にアクセスできることを確認するテスト
    @pytest.mark.django_db
    def test_correct_user_acces_success(self):
        c = client.Client()
        token = self.login()
        # トークンをヘッダーにセットして収支一覧ページにアクセス
        response = c.get(path= self.PATH,  HTTP_AUTHORIZATION = 'jwt ' + token)
    
        assert response.status_code == 200
        
    
    # 収支一覧ページにアクセスした場合、
    @pytest.mark.django_db
    def test_add_spending_success(self):
        token = self.login()
        
        c = client.Client()
    
        data = {
            "date":"2022-9-23",
            "name":"レコード名１",
            "category":"カテゴリー名１",
            "memo":"メモ１",
        } 
        
        # 開始時の収支一覧の件数を取得
        before_count = Spending.objects.all().count()
        
        response = c.post(path= self.PATH,  HTTP_AUTHORIZATION = 'jwt ' + token, data=data)
        
        # 登録後の収支一覧の件数を取得
        after_count = Spending.objects.all().count() 
        # assert response.status_code == 201 
        assert after_count - before_count == 1
        
# 収支詳細ページのテスト
class Test_Spending_Detail_Page:
    BASE_PATH = '/api/spending/'
    
    # ログイン処理
    @staticmethod
    def login():
        c = client.Client()
        data = {
            "username": "MrPython",
            "password":"password1234",
        }
        token = ast.literal_eval(c.post(path= '/api/user/login/',data=data).content.decode('utf-8'))['token']
        
        return token
    
   # データの登録
    @pytest.fixture(autouse=True, scope='class')
    def setUp(self, django_db_setup, django_db_blocker):
        with django_db_blocker.unblock():
                 # # fixturesからデータを読んでDBに入れる
                call_command('loaddata', 'tests/fixtures/users.json')
                call_command('loaddata', 'tests/fixtures/spendings.json')
                
    # ログインせず収支詳細ページにアクセスした場合、閲覧禁止エラーが返却されることを確認するテスト
    def test_bad_user_acces_denied(self):
        c = client.Client()
        response = c.get(path = self.BASE_PATH+'1/')

        assert response.status_code == 403
        
    # ログインしている状態で収支詳細ページにアクセスした場合、正常にアクセスできることを確認するテスト
    @pytest.mark.django_db
    def test_correct_user_access_success(self):
        # ログイン
        token = self.login()
        
        c = client.Client()
        response = c.get(path=self.BASE_PATH + '1/', HTTP_AUTHORIZATION = 'jwt ' + token)
        
        assert response.status_code == 200
        
    # ログインしている状態で存在しない収支詳細ページにアクセスした場合、404エラーが返却されることを確認するテスト
    @pytest.mark.django_db
    def test_correct_user_access_success(self):
        # ログイン
        token = self.login()
        
        c = client.Client()
        response = c.get(path=self.BASE_PATH + '1000/', HTTP_AUTHORIZATION = 'jwt ' + token)
        
        assert response.status_code == 404