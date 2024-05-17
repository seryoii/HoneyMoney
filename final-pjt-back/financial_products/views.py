from django.shortcuts import render
from rest_framework.decorators import api_view
from django.conf import settings
from rest_framework.response import Response
from django.http import HttpResponse
from .serializers import DepositSerializer
import requests
API_KEY = settings.API_KEY
# API_KEY='075aba31f295dc17f85b416dfabc2969'
# Create your views here.

@api_view(['GET'])
def get_deposit_products(request):
    deposit_API_URL = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'

    deposit_baselist = requests.get(deposit_API_URL).json().get('result').get('baseList')
    deposit_optionlist = requests.get(deposit_API_URL).json().get('result').get('optionList')
    for data in deposit_baselist:
        print(data['fin_prdt_cd'])
        deposit_product = {
            'fin_prdt_cd': data.get('fin_prdt_cd'),
            'fin_co_no': data.get('fin_co_no'),
            'kor_co_nm': data.get('kor_co_nm'),
            'fin_prdt_nm': data.get('fin_prdt_nm'),
            'join_way': data.get('join_way'),
            'mtrt_int': data.get('mtrt_int'),
            'spcl_cnd': data.get('spcl_cnd'),
            'join_deny': data.get('join_deny'),
            'join_member': data.get('join_member'),
            'etc_note': data.get('etc_note'),
            'max_limit': data.get('max_limit')
        }
        serializer = DepositSerializer(data=deposit_product)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return HttpResponse(deposit_product)
    # return Response(deposit_baselist)
@api_view(['GET'])
def get_saving_products(request):
    saving_API_URL = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    saving_baselist = requests.get(saving_API_URL).json()['result']['baseList']
    saving_optionlist = requests.get(saving_API_URL).json()['result']['optionList']

    return Response(saving_baselist)
