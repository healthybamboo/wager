import os
import pytest
import ast
from django.test import client
import json
from django.core.management import call_command

from api.models import Bed, Game
'''
=================================
ゲーム一覧ページについてのテスト
(GET)->ゲームの一覧を取得する,
(POST)->ゲームを新規作成する,
=================================
'''


#  ゲーム一覧ページのテスト
class Test_GET_GAME_List_Page:
    PATH = '/api/games/'

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
            #  fixturesからデータを読んでDBに入れる
            call_command('loaddata', 'tests/fixtures/users.json')
            call_command('loaddata', 'tests/fixtures/tags.json')
            call_command('loaddata', 'tests/fixtures/bedways.json')
            call_command('loaddata', 'tests/fixtures/games.json')
            call_command('loaddata', 'tests/fixtures/beds.json')

    # (GET)ログインせずにゲーム一覧ページにアクセスした場合、閲覧禁止エラーが返却されることを確認するテスト
    @pytest.mark.django_db
    def test_unknown_user_acces_denied(self):
        c = client.Client()
        response = c.get(self.PATH)

        assert response.status_code == 403

    # (GET)ログインした状態でゲーム一覧ページにアクセスした場合、正常にアクセスできることを確認するテスト
    @pytest.mark.django_db
    def test_correct_user_access_success(self):
        token = self.login()

        c = client.Client()
        response = c.get(self.PATH, HTTP_AUTHORIZATION='jwt ' + token)

        assert response.status_code == 200

    # (GET)gamesが取得できることを確認するためのテスト
    @pytest.mark.django_db
    def test_get_games(self):
        # ログイン
        token = self.login()

        # APIを叩く
        c = client.Client()
        response = c.get(self.PATH, HTTP_AUTHORIZATION='jwt ' + token)

        # 想定されるデータ(一応jsonに直しておく)
        EXPECTED = json.dumps([{
            "id": 1,
            "name": "掛け方まる１",
            "way": 1,
            "unit": 100,
            "state": {
                "current": [1, 3, 4, 5, 6]
            },
            "archive": False
        }])

        assert response.data[0] == EXPECTED[0]


# ゲームの登録に関するテスト
class Test_POST_Bed_List_View:
    PATH = '/api/games/'

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
            #  fixturesからデータを読んでDBに入れる
            call_command('loaddata', 'tests/fixtures/users.json')
            call_command('loaddata', 'tests/fixtures/tags.json')
            call_command('loaddata', 'tests/fixtures/bedways.json')
            call_command('loaddata', 'tests/fixtures/games.json')
            call_command('loaddata', 'tests/fixtures/beds.json')

    # (POST)ログインせずに、ゲームの追加を行おうとした場合は403エラーが帰る
    @pytest.mark.django_db
    def test_unknown_user_create_game(self):
        data = {
            "model": "api.game",
            "pk": 1,
            "fields": {
                "user": 1,
                "name": "name",
                "way": 1,
                "unit": 100,
                "state": {
                    "current": [1, 3, 4, 5, 6]
                },
                "archive": False
            }
        }

        c = client.Client()
        response = c.post(path=self.PATH,
                          data=data,
                          content_type='application/json')

        assert response.status_code == 403

    # (POST)ログインしてデータの追加をしようとした場合、成功することを確認する
    @pytest.mark.django_db
    def test_correct_users_cat_create_game(self):
        #　ログイン
        token = self.login()

        # 送信するデータ,userとかstateはGameの作成時にはしない
        DATA = {
            "name": "掛け方まる３",
            "way": 1,
            "unit": 100,
        }

        EXPEDTED = {
            'id': 3,
            'name': '掛け方まる３',
            'way': 1,
            'unit': 100,
            'state': None,
            'archive': False
        }

        before_count = Game.objects.count()

        # 接続する
        c = client.Client()
        response = c.post(path=self.PATH,
                          data=DATA,
                          HTTP_AUTHORIZATION='jwt ' + token,
                          content_type='application/json')

        after_count = Game.objects.count()
        # 正しいステータスコードが帰ってくることを確認する
        assert response.status_code == 201

        # データが登録されていることを確認する
        assert after_count - before_count == 1

        # 登録後にデータが返されることを確認する
        assert response.data == EXPEDTED
