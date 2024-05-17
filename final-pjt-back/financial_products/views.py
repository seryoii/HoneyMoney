from django.shortcuts import render
from rest_framework.decorators import api_view
from django.conf import settings
from rest_framework.response import Response
from django.http import HttpResponse
from .serializers import DepositSerializer, DepositOptionSerializer, SavingSerializer, SavingOptionSerializer
import requests
from .models import DepositProduct, SavingProduct
API_KEY = settings.FIN_API_KEY
# API_KEY='075aba31f295dc17f85b416dfabc2969'
# Create your views here.

@api_view(['GET'])
def get_deposit_products(request):
    deposit_API_URL = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'

    deposit_baselist = requests.get(deposit_API_URL).json().get('result').get('baseList')
    deposit_optionlist = requests.get(deposit_API_URL).json().get('result').get('optionList')

    # return Response(deposit_baselist)   

    for base in deposit_baselist:
        # if DepositProduct.objects.filter(fin_prdt_cd=base.get('fin_prdt_cd')):
        #     continue
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
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    for option in deposit_optionlist:
        prdt_cd = option.get('fin_prdt_cd')
        products = DepositProduct.objects.filter(fin_prdt_cd=prdt_cd)
        print(product)
        for product in products:
            deposit_option = {
                'intr_rate_type': option.get('intr_rate_type'),
                'intr_rate_type_nm': option.get('intr_rate_type_nm'),
                'save_trm': option.get('save_trm'),
                'intr_rate': option.get('intr_rate'),
                'intr_rate2': option.get('intr_rate2'),  
            }
            serializer = DepositOptionSerializer(data=deposit_option)
            if serializer.is_valid(raise_exception=True):
                serializer.save(deposit_product=product)
                # return Response(deposit_option)
        
@api_view(['GET'])
def get_saving_products(request):
    saving_API_URL = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    saving_baselist = requests.get(saving_API_URL).json()['result']['baseList']
    saving_optionlist = requests.get(saving_API_URL).json()['result']['optionList']

    for base in saving_baselist:
        saving_product = {
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
        serializer = SavingSerializer(data=saving_product)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    for option in saving_optionlist:
        prdt_cd = option.get('fin_prdt_cd')
        products = SavingProduct.objects.filter(fin_prdt_cd=prdt_cd)
        print(product)
        for product in products:
            saving_option = {
                'intr_rate_type': option.get('intr_rate_type'),
                'intr_rate_type_nm': option.get('intr_rate_type_nm'),
                'rsrv_type': option.get('rsrv_type'),
                'rsrv_type_nm': option.get('rsrv_type_nm'),
                'save_trm': option.get('save_trm'),
                'intr_rate': option.get('intr_rate'),
                'intr_rate2': option.get('intr_rate2'),  
            }
            serializer = SavingOptionSerializer(data=saving_option)
            if serializer.is_valid(raise_exception=True):
                serializer.save(saving_product=product)

@api_view(['GET'])
def deposit_product_list(request):
    if request.method == 'GET':
        deposit_products = DepositProduct.objects.all()
        serializer = DepositSerializer(deposit_products, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def saving_product_list(request):
    if request.method == 'GET':
        saving_products = SavingProduct.objects.all()
        serializer = DepositSerializer(saving_products, many=True)
        return Response(serializer.data)
