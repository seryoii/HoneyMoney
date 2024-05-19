from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
# Create your views here.
EXCHANGE_API_KEY = settings.EXCHANGE_API_KEY

@api_view(['GET'])
def exchange(request):
    # API_URL = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={EXCHANGE_API_KEY}&data=AP01'
    API_URL = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={EXCHANGE_API_KEY}&searchdate=20220516&data=AP01'

    result = requests.get(API_URL).json()

    return Response(result)
