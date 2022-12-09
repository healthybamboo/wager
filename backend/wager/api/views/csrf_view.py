from rest_framework.response import Response
from django.middleware.csrf import get_token
from rest_framework.decorators import api_view

# CSRFを取得する処理
@api_view(['GET'])
def csrf_view(request):
    return Response(data={'csrfToken': get_token(request)})