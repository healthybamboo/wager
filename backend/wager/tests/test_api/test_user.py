import os
from django.test import client
import pytest
from django.core.management import  call_command

# ユーザー登録が正常に行われることを確認するテスト
class Test_CreateUser:
    PATH = '/api/user/signup/'
    @pytest.fixture(autouse=True, scope='class')
    def setUp(self, django_db_setup, django_db_blocker):
        with django_db_blocker.unblock():
                 # # fixturesからデータを読んでDBに入れる
                call_command('loaddata', 'tests/fixtures/users.json')

    # ユーザーが正常に登録されることを確認するテスト
    @pytest.mark.django_db
    def test_create_user(self):
        data = {
            "username": "python",
            "email":"testmail@example.com",
            "password": "password1234", 
            }
        
        c = client.Client()
        response = c.post(self.PATH, data=data, content_type='application/json')

        assert response.status_code == 201
    
    # 既に登録されているユーザー名で登録しようとした場合にエラーが返ってくることを確認するテスト
    @pytest.mark.django_db
    def test_create_user_with_same_name(self):
        data = {
            "username": "MrPython",
            "email":"test@example.com",
            "password": "password1234", 
            }
        
        c = client.Client()
        

        response = c.post(self.PATH, data=data, content_type='application/json')
        
        assert response.status_code == 409


# ユーザー情報の更新が正常に行われることを確認するテスト
class Test_UpdateUser:
    PATH = '/api/user/update/'
    # データベースの初期化
    @pytest.fixture(autouse=True, scope='class')
    def setUp(self, django_db_setup, django_db_blocker):
        with django_db_blocker.unblock():
                 # # fixturesからデータを読んでDBに入れる
                call_command('loaddata', 'tests/fixtures/users.json')
                
    # ユーザー情報の更新が正常に行われることを確認するテスト
    @pytest.mark.skip
    @pytest.mark.django_db
    def test_update_user_info(self):
        data = {
            "email":"test@example.com",
            "password": "password1234", 
        }
        
        c = client.Client()
        
        response = c.put(self.PATH, data=data, content_type='application/json')
       
        assert response.status_code == 200
        
    # TODO.ユーザー情報の更新が失敗することを確認するテスト
        
        
        
# ユーザーログインが正常に行われることを確認するテスト
class Test_Login:
    
    PATH = '/api/user/login/'

    @pytest.fixture(autouse=True, scope='class')
    def setUp(self, django_db_setup, django_db_blocker):
        with django_db_blocker.unblock():
                 # # fixturesからデータを読んでDBに入れる
                call_command('loaddata', 'tests/fixtures/users.json')
            
    # ログインが正しいユーザーならばログインが成功することを確認するテスト
    @pytest.mark.django_db
    def test_login_success(self):
        data = {
        "username": "MrPython",
        "password": "password1234", 
         }
        
        c = client.Client()
        response = c.post(self.PATH, data=data)

        assert response.status_code == 200
        
    # 誤ったユーザならばログインが失敗することを確認するテスト
    @pytest.mark.django_db
    def test_login_bad_user(self):
        data = {
        "username": "daredesuka",
        "password": "password1234", 
         }
        
        c = client.Client()
        response = c.post(self.PATH, data=data)

        assert response.status_code == 403
        
    # 誤ったパスワードならばログインが失敗することを確認するテスト
    @pytest.mark.django_db
    def test_login_bad_pass(self):
        data = {
            "username": "daredesuka",
            "password": "password1234", 
            }
        c = client.Client()
        response = c.post(self.PATH, data=data)

        assert response.status_code == 403
        

            
     