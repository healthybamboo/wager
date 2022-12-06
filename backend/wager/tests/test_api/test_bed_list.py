import pytest
import ast
from django.test import client
from django.core.management import call_command
from api.models import Bed
'''
=================================
収支一覧ページについてのテスト
(GET) -> 収支の一覧を取得する,
TODO.(POST)-> 収支を新規作成する,
=================================
'''


#  (GET)収支一覧ページのテスト
class Test_GET_Bed_List_Page:
    PATH = '/api/beds/'

    # ログイン処理
    @staticmethod
    def login():
        c = client.Client()
        data = {
            "username": "MrPython",
            "password": "password1234",
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

    # (GET)ログインせず収支一覧ページにアクセスした場合、閲覧禁止エラーが返却されることを確認するテスト
    def test_bad_user_acces_denied(self):
        c = client.Client()
        response = c.get(self.PATH)

        assert response.status_code == 403

    # (GET)ログインした状態で収支一覧ページにアクセスした場合、正常にアクセスできることを確認するテスト
    @pytest.mark.django_db
    def test_correct_user_acces_success(self):
        c = client.Client()
        token = self.login()
        # トークンをヘッダーにセットして収支一覧ページにアクセス
        response = c.get(self.PATH, {"year":2022,"month":12,"day":6 },HTTP_AUTHORIZATION='jwt ' + token)

        assert response.status_code == 200


class Test_POST_Bed_List_Page:
    PATH = '/api/beds/'

    # ログイン処理
    @staticmethod
    def login():
        c = client.Client()
        data = {
            "username": "MrPython",
            "password": "password1234",
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

    # (POST)収支一覧ページで追加した場合、正常に追加できることを確認するテスト
    @pytest.mark.django_db
    def test_add_bed_success(self):
        token = self.login()

        c = client.Client()

        data = {
            "date": "2022-9-23",
            "name": "レコード名１",
            "spend": 100,
            "refund": 0,
            "memo": "メモ１",
        }

        # 開始時の収支一覧の件数を取得
        before_count = Bed.objects.all().count()

        response = c.post(path=self.PATH,
                          HTTP_AUTHORIZATION='jwt ' + token,
                          data=data)

        # 登録後の収支一覧の件数を取得
        after_count = Bed.objects.all().count()
        # assert response.status_code == 201
        assert after_count - before_count == 1
