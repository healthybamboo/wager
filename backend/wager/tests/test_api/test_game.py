import os
from django.test import client
import pytest
from django.core.management import call_command
from api.models import Game
import ast
'''
=================================
ユーザーについてのテスト
(GET)->ゲームの詳細を取得する
(PUT)->ゲームの情報を更新する
(DELET)->ゲームを削除する,
=================================
'''


# ゲームの詳細に関するテスト
class Test_GET_Game:
    BASE_PATH = '/api/games/'

    # ログイン処理
    @staticmethod
    def login(username="MrPython", password="password1234"):
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
            #  fixturesからデータを読んでDBに入れる
            call_command('loaddata', 'tests/fixtures/users.json')
            call_command('loaddata', 'tests/fixtures/tags.json')
            call_command('loaddata', 'tests/fixtures/bedways.json')
            call_command('loaddata', 'tests/fixtures/games.json')
            call_command('loaddata', 'tests/fixtures/beds.json')

    # (GET)ログインせずにゲーム詳細ページにアクセスした場合、閲覧禁止エラーが返却されることを確認するテスト(GET)
    @pytest.mark.django_db
    def test_unknown_user_acces_denied(self):
        c = client.Client()
        response = c.get(path=self.BASE_PATH + '1/')

        assert response.status_code == 403

    # (GET)所有者以外がゲーム詳細ページにアクセスした場合、閲覧禁止エラーが返却されることを確認するテスト(GET)
    @pytest.mark.django_db
    def test_bad_user_acces_denied(self):
        token = self.login(username="tkr1234", password="password1234")
        c = client.Client()
        response = c.get(path=self.BASE_PATH + '1/',
                         HTTP_AUTHORIZATION='jwt ' + token)

        assert response.status_code == 403

    # (GET)ログインした状態でゲーム詳細ページにアクセスした場合、正常にアクセスできることを確認するテスト
    @pytest.mark.django_db
    def test_correct_user_access_success(self):
        token = self.login()

        c = client.Client()
        response = c.get(path=self.BASE_PATH + '1/',
                         HTTP_AUTHORIZATION='jwt ' + token)

        assert response.status_code == 200

    # (GET)存在しないゲームの詳細ページにアクセスした場合、404エラーが返却されることを確認するテスト
    @pytest.mark.django_db
    def test_not_exist_game(self):
        token = self.login()

        c = client.Client()
        response = c.get(path=self.BASE_PATH + '1000/',
                         HTTP_AUTHORIZATION='jwt ' + token)

        assert response.status_code == 404

    # (GET)正しいゲームの詳細情報が返ってきているかを確認するテスト
    @pytest.mark.django_db
    def test_correct_user_access_success(self):
        token = self.login()

        EXPECTED = {
            'id': 1,
            'name': '掛け方まる１',
            'way': 1,
            'unit': 100,
            'state': {
                'current': [1, 3, 4, 5, 6]
            },
            'archive': False
        }

        c = client.Client()
        response = c.get(path=self.BASE_PATH + '1/',
                         HTTP_AUTHORIZATION='jwt ' + token)
        assert response.data == EXPECTED


# ゲームの更新処理に関するテスト
class Test_PUT_Game:
    BASE_PATH = '/api/games/'

    # ログイン処理
    @staticmethod
    def login(username="MrPython", password="password1234"):
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
            #  fixturesからデータを読んでDBに入れる
            call_command('loaddata', 'tests/fixtures/users.json')
            call_command('loaddata', 'tests/fixtures/tags.json')
            call_command('loaddata', 'tests/fixtures/bedways.json')
            call_command('loaddata', 'tests/fixtures/games.json')
            call_command('loaddata', 'tests/fixtures/beds.json')

    # (PUT)ゲームの情報を更新するテスト
    @pytest.mark.django_db
    def test_correct_user_access_success(self):
        token = self.login()

        data = {
            'name': '掛け方まる２(更新)',
        }

        EXPECTED = {
            'id': 2,
            'name': '掛け方まる２(更新)',
            'way': 1,
            'unit': 100,
            'state': {
                'current': [1, 3, 4, 5, 6]
            },
            'archive': False
        }

        c = client.Client()

        # 更新前のデータを取得
        response = c.put(path=self.BASE_PATH + '2/',
                         HTTP_AUTHORIZATION='jwt ' + token,
                         data=data,
                         content_type='application/json')

        # ステータスが200であることを確認
        assert response.status_code == 200

        # 返ってきたデータが期待通りであることを確認
        assert response.data == EXPECTED

        # データベースのデータが更新されていることを確認
        assert Game.objects.get(id=2).name == '掛け方まる２(更新)'

    # (PUT)所有者以外がゲーム詳細ページを更新しようとした場合場合、閲覧禁止エラーが返却されることを確認するテスト(GET)
    @pytest.mark.django_db
    def test_bad_user_acces_denied(self):
        token = self.login(username="tkr1234", password="password1234")
        c = client.Client()
        response = c.put(path=self.BASE_PATH + '1/',
                         HTTP_AUTHORIZATION='jwt ' + token)

        assert response.status_code == 403


# ゲームの削除に関するテスト
class Test_DELETE_Game:
    BASE_PATH = '/api/games/'

    # ログイン処理
    @staticmethod
    def login(username="MrPython", password="password1234"):
        c = client.Client()
        data = {
            "username": username,
            "password": password,
        }
        token = ast.literal_eval(
            c.post(path='/api/user/login/',
                   data=data).content.decode('utf-8'))['token']

        return token

    # (DELETE)データの登録
    @pytest.fixture(autouse=True, scope='class')
    def setUp(self, django_db_setup, django_db_blocker):
        with django_db_blocker.unblock():
            #  fixturesからデータを読んでDBに入れる
            call_command('loaddata', 'tests/fixtures/users.json')
            call_command('loaddata', 'tests/fixtures/tags.json')
            call_command('loaddata', 'tests/fixtures/bedways.json')
            call_command('loaddata', 'tests/fixtures/games.json')
            call_command('loaddata', 'tests/fixtures/beds.json')

    # (DELETE)レコードの削除が正常に行われるかを確認するテスト
    @pytest.mark.django_db
    def test_delete_game_succees(self):
        token = self.login()

        ID = 1
        # 事前にデータが存在していることを確認
        game = Game.objects.filter(id=ID).first()
        assert game is not None

        # 削除処理
        c = client.Client()
        response = c.delete(path=self.BASE_PATH + str(ID) + '/',
                            HTTP_AUTHORIZATION='jwt ' + token)

        # ステータスコードの確認
        assert response.status_code == 200

        # 削除されていることを確認
        game = Game.objects.filter(id=ID).first()
        assert game is None

    # (DELETE)存在しないゲームの詳細ページにアクセスした場合、404エラーが返却されることを確認するテスト
    @pytest.mark.django_db
    def test_not_exist_game(self):
        # ログイン
        token = self.login()

        # 削除処理
        c = client.Client()
        response = c.delete(path=self.BASE_PATH + '1000/',
                            HTTP_AUTHORIZATION='jwt ' + token)

        assert response.status_code == 404

    #　(DELETE)所有者以外のユーザーが削除しようとした場合に403エラーが返却されることを確認するテスト
    @pytest.mark.django_db
    def test_not_exist_game(self):
        # ログイン
        token = self.login(username="tkr1234", password="password1234")

        c = client.Client()
        response = c.delete(path=self.BASE_PATH + '1/',
                            HTTP_AUTHORIZATION='jwt ' + token)

        assert response.status_code == 403
