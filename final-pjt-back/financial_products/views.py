from django.shortcuts import render
from rest_framework.decorators import api_view
from django.conf import settings
from django.http import HttpResponse
from rest_framework.response import Response
import requests
API_KEY = settings.API_KEY
# API_KEY='075aba31f295dc17f85b416dfabc2969'
# Create your views here.

@api_view(['GET'])
def get_deposit_products(request):
    deposit_API_URL = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'

    deposit_baselist = requests.get(deposit_API_URL).json()['result']['baseList']
    return Response(deposit_baselist)

@api_view(['GET'])
def get_saving_products(request):
    saving_API_URL = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    saving_baselist = requests.get(saving_API_URL).json()['result']['baseList']
    return Response(saving_baselist)
