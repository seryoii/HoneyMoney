from django.shortcuts import render
from rest_framework.decorators import api_view
from django.conf import settings
from rest_framework.response import Response
from django.http import HttpResponse
from .serializers import DepositSerializer
import requests
from .models import DepositProduct
API_KEY = settings.FIN_API_KEY
# API_KEY='075aba31f295dc17f85b416dfabc2969'
# Create your views here.

@api_view(['GET'])
def get_deposit_products(request):
    deposit_API_URL = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'

    deposit_baselist = requests.get(deposit_API_URL).json().get('result').get('baseList')
    deposit_optionlist = requests.get(deposit_API_URL).json().get('result').get('optionList')
    for base in deposit_baselist:
        deposit_product = {
            'fin_prdt_cd': base.get('fin_prdt_cd'),
            'fin_co_no': base.get('fin_co_no'),
            'kor_co_nm': base.get('kor_co_nm'),
            'fin_prdt_nm': base.get('fin_prdt_nm'),
            'join_way': base.get('join_way'),
            'mtrt_int': base.get('mtrt_int'),
            'spcl_cnd': base.get('spcl_cnd'),
            'join_deny': base.get('join_deny'),
            'join_member': base.get('join_member'),
            'etc_note': base.get('etc_note'),
            'max_limit': base.get('max_limit')
        }
        serializer = DepositSerializer(data=deposit_product)
        # if serializer.is_valid(raise_exception=True):
        #     serializer.save()
        #     return Response(deposit_product)
        
    # return Response(deposit_optionlist)
    for option in deposit_optionlist:
        prdt_cd = option.get('fin_prdt_cd')
        product = DepositProduct.objects.get(fin_prdt_cd=prdt_cd)
        print(product)
        # return Response(product)

    # return Response(deposit_optionlist)
@api_view(['GET'])
def get_saving_products(request):
    saving_API_URL = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    saving_baselist = requests.get(saving_API_URL).json()['result']['baseList']
    saving_optionlist = requests.get(saving_API_URL).json()['result']['optionList']

    return Response(saving_baselist)
