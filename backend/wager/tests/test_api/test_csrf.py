import os
import pytest
import ast
from django.test import client
from django.core.management import call_command
from api.models import Bed

'''
=================================
CSRFトークンの取得に関するテスト
=================================
'''

class Test_GET_csrf_token:
    # アクセスが正しくできているかを確認するテスト
    def test_access_is_success(self):
        c = client.Client()
        response = c.get(path='/api/csrf/')
        assert response.status_code == 200
    
    # トークンが正しい長さで取得できているかどうか
    def test_can_get_csrf_token(self):
        c = client.Client()
        response = c.get(path='/api/csrf/')
        assert len(response.data['csrfToken'] ) == 64
