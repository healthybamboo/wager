import os
import pytest
import ast
from django.test import client
from django.core.management import call_command
from api.models import Bed
'''
=================================
収支詳細ページについてのテスト
(GET)->IDで指定した収支を取得する,
TODO.(PUT)->IDで指定した収支を更新する,
=================================
'''


# (GET) 収支詳細ページのテスト
class Test_GET_Bed:
    BASE_PATH = '/api/beds/'

    # ログイン処理
    @staticmethod
    def login(username: str = "MrPython", password: str = "password1234"):
        c = client.Client()
        data = {
            "username": username,
            "password": password,
        }
        token = ast.literal_eval(
            c.post(path='/api/user/login/',
                   data=data).content.decode('utf-8'))['token']

        return token

    # データの登録
    @pytest.fixture(autouse=True, scope='class')
    def setUp(self, django_db_setup, django_db_blocker):
        with django_db_blocker.unblock():
            # # fixturesからデータを読んでDBに入れる
            call_command('loaddata', 'tests/fixtures/users.json')
            call_command('loaddata', 'tests/fixtures/beds.json')

    # (GET)ログインせず収支詳細ページにアクセスした場合、閲覧禁止エラーが返却されることを確認するテスト
    def test_unknown_user_acces_denied(self):
        c = client.Client()
        response = c.get(path=self.BASE_PATH + '1/')

        assert response.status_code == 403

    # (GET)ログインしている状態で収支詳細ページにアクセスした場合、正常にアクセスできることを確認するテスト
    @pytest.mark.django_db
    def test_correct_user_access_success(self):
        # ログイン
        token = self.login()

        c = client.Client()
        response = c.get(path=self.BASE_PATH + '1/',
                         HTTP_AUTHORIZATION='jwt ' + token)

        assert response.status_code == 200

    # (GET)存在しない収支詳細ページにアクセスした場合、404エラーが返却されることを確認するテスト(GET)
    @pytest.mark.django_db
    def test_access_not_exist_bed(self):
        # ログイン
        token = self.login()

        c = client.Client()
        response = c.get(path=self.BASE_PATH + '1000/',
                         HTTP_AUTHORIZATION='jwt ' + token)

        assert response.status_code == 404

    # (GET)作成者とは別のユーザーが収支詳細ページにアクセスしようとした場合、403エラーが返却されることを確認するテスト(GET)
    @pytest.mark.django_db
    def test_bad_user_acces_denied(self):
        # ログイン
        token = self.login(username="tkr1234", password="password1234")

        c = client.Client()
        response = c.get(path=self.BASE_PATH + '1/',
                         HTTP_AUTHORIZATION='jwt ' + token)

        assert response.status_code == 403

'''
class Test_PUT_Bed:
    BASE_PATH = '/api/beds/'

    # ログイン処理
    @staticmethod
    def login(username: str = "MrPython", password: str = "password1234"):
        c = client.Client()
        data = {
            "username": username,
            "password": password,
        }
        token = ast.literal_eval(
            c.post(path='/api/user/login/',
                   data=data).content.decode('utf-8'))['token']

        return token

    # データの登録
    @pytest.fixture(autouse=True, scope='class')
    def setUp(self, django_db_setup, django_db_blocker):
        with django_db_blocker.unblock():
            # # fixturesからデータを読んでDBに入れる
            call_command('loaddata', 'tests/fixtures/users.json')
            call_command('loaddata', 'tests/fixtures/beds.json')

    # (PUT)ログインせず収支詳細ページにアクセスした場合、閲覧禁止エラーが返却されることを確認するテスト
    def test_unknown_user_acces_denied(self):
        c = client.Client()
        response = c.put(path=self.BASE_PATH + '1/')

        assert response.status_code == 403

    # (PUT)ログインしている状態で収支詳細ページにアクセスした場合、正常にアクセスできることを確認するテスト
    @pytest.mark.django_db
    def test_correct_user_access_success(self):
        # ログイン
        token = self.login()

        c = client.Client()
        response = c.put(path=self.BASE_PATH + '1/',
                         HTTP_AUTHORIZATION='jwt ' + token)

        assert response.status_code == 200

    # (PUT)存在しない収支詳細ページにアクセスした場合、404エラーが返却されることを確認するテスト
    @pytest.mark.django_db
    def test_access_not_exist_bed(self):
        # ログイン
        token = self.login()

        c = client.Client()
        response = c.put(path=self.BASE_PATH + '1000/',
                         HTTP_AUTHORIZATION='jwt ' + token)

        assert response.status_code == 404

    # (PUT)作成者とは別のユーザーが収支詳細ページにアクセスしようとした場合、403エラーが返却されることを確認するテスト
    @pytest.mark.django_db
    def test_bad_user_acces_denied(self):
        # ログイン
        token = self.login(username="tkr1234", password="password1234")

        c = client.Client()
        response = c.put(path=self.BASE_PATH + '1/',
                         HTTP_AUTHORIZATION='jwt ' + token)

        assert response.status_code == 403
'''