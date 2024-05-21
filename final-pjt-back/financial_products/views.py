from django.http import JsonResponse
import requests
import random

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DepositSerializer, DepositOptionSerializer, DepositListSerializer, InterestDepositSerializer, DepositRecommendSerializer
from .serializers import SavingSerializer, SavingOptionSerializer, SavingListSerializer, InterestSavingSerializer, SavingRecommendSerializer
from .models import DepositProduct, SavingProduct, DepositOption, SavingOption
from accounts.models import User


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
        if DepositProduct.objects.filter(fin_prdt_cd=base.get('fin_prdt_cd')):
            continue
        deposit_product = {
            'dcls_month' : base.get('dcls_month'),
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
    # return Response(deposit_baselist)
    for option in deposit_optionlist:
        prdt_cd = option.get('fin_prdt_cd')
        products = DepositProduct.objects.filter(fin_prdt_cd=prdt_cd)
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
    return Response('Deposit 데이터 가져오기 성공')

@api_view(['GET'])
def get_saving_products(request):
    saving_API_URL = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    saving_baselist = requests.get(saving_API_URL).json()['result']['baseList']
    saving_optionlist = requests.get(saving_API_URL).json()['result']['optionList']

    for base in saving_baselist:
        if SavingProduct.objects.filter(fin_prdt_cd=base.get('fin_prdt_cd')):
            continue
        saving_product = {
            'dcls_month' : base.get('dcls_month'),
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
    return Response('Saving 데이터 가져오기 성공')

@api_view(['GET'])
def deposit_product_list(request):
    if request.method == 'GET':
        deposit_products = DepositProduct.objects.all()
        serializer = DepositListSerializer(deposit_products, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def saving_product_list(request):
    if request.method == 'GET':
        saving_products = SavingProduct.objects.all()
        serializer = SavingListSerializer(saving_products, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def deposit_detail(request, deposit_name):
    deposit = get_object_or_404(DepositProduct, fin_prdt_nm=deposit_name)
    if request.method == 'GET':
        serializer = DepositSerializer(deposit)
        return Response(serializer.data)
    
@api_view(['GET'])
def saving_detail(request, saving_name):
    saving = get_object_or_404(SavingProduct, fin_prdt_nm=saving_name)
    if request.method == 'GET':
        serializer = SavingSerializer(saving)
        return Response(serializer.data)
    
@api_view(['GET'])
def deposit_option_list(request, deposit_code):
    deposit = get_object_or_404(DepositProduct, fin_prdt_cd=deposit_code)
    deposit_options = DepositOption.objects.filter(deposit_product=deposit)

    if request.method == 'GET':
        serializer = DepositOptionSerializer(deposit_options, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def deposit_option_detail(request, deposit_code, option_id):
    deposit = get_object_or_404(DepositProduct, fin_prdt_cd=deposit_code)
    option = DepositOption.objects.get(deposit_product=deposit, id=option_id)
    if request.method == 'GET':
        serializer = DepositOptionSerializer(option)
        return Response(serializer.data)

    
@api_view(['GET'])
def saving_option_list(request, saving_name):
    saving = get_object_or_404(SavingProduct, fin_prdt_nm=saving_name)
    saving_options = SavingOption.objects.filter(saving_product=saving)

    if request.method == 'GET':
        serializer = SavingOptionSerializer(saving_options, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def saving_option_detail(request, saving_code, option_id):
    saving = get_object_or_404(SavingProduct, fin_prdt_cd=saving_code)
    option = SavingOption.objects.get(saving_product=saving, id=option_id)
    if request.method == 'GET':
        serializer = SavingOptionSerializer(option)
        return Response(serializer.data)

# @api_view(['GET', 'POST', 'DELETE'])
# def deposit_interest(request, deposit_code):
#     deposit = get_object_or_404(DepositProduct, fin_prdt_cd=deposit_code)
#     if request.method == 'GET':
#         serializer = InterestDepositSerializer(deposit)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         if request.user not in deposit.interest_user.all():
#             deposit.interest_user.add(request.user)
#             serializer = InterestDepositSerializer(deposit, data=request.data, partial=True)

#             if serializer.is_valid(raise_exception=True):
#                 serializer.save()
#                 return Response({ "detail": "상품이 추가되었습니다." }, status=status.HTTP_200_OK)
#         else:
#             return Response({ "detail": "이미 상품이 존재합니다." }, status=status.HTTP_400_BAD_REQUEST)
        
#     elif request.method == 'DELETE':
#         if request.user in deposit.interest_user.all():
#             deposit.interest_user.remove(request.user)
#             return Response({ "detail": "삭제되었습니다." }, status=status.HTTP_204_NO_CONTENT)
#         else:
#             return Response({ "detail": "삭제할 항목이 없습니다." }, status=status.HTTP_404_NOT_FOUND)

# @api_view(['GET', 'POST', 'DELETE'])
# def saving_interest(request, saving_code):
#     saving = get_object_or_404(DepositProduct, fin_prdt_cd=saving_code)
#     if request.method == 'GET':
#         serializer = InterestSavingSerializer(saving)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         if request.user not in saving.interest_user.all():
#             saving.interest_user.add(request.user)
#             serializer = InterestSavingSerializer(saving, data=request.data, partial=True)

#             if serializer.is_valid(raise_exception=True):
#                 serializer.save()
#                 return Response({ "detail": "상품이 추가되었습니다." }, status=status.HTTP_200_OK)
#         else:
#             return Response({ "detail": "이미 상품이 존재합니다." }, status=status.HTTP_400_BAD_REQUEST)
        
#     elif request.method == 'DELETE':
#         if request.user in saving.interest_user.all():
#             saving.interest_user.remove(request.user)
#             return Response({ "detail": "삭제되었습니다." }, status=status.HTTP_204_NO_CONTENT)
#         else:
#             return Response({ "detail": "삭제할 항목이 없습니다." }, status=status.HTTP_404_NOT_FOUND)
        
@api_view(['GET'])
def bank_deposit(request, bank_name):
    if request.method == 'GET':
        if DepositProduct.objects.filter(kor_co_nm=bank_name).exists():
            deposits = DepositProduct.objects.filter(kor_co_nm=bank_name)
            serializer = DepositListSerializer(deposits, many=True)
            return Response(serializer.data)
        else:
            return Response({'detail': '해당 은행의 상품이 없습니다.'}, status=status.HTTP_204_NO_CONTENT)
        
@api_view(['GET'])
def bank_saving(request, bank_name):
    if request.method == 'GET':
        if SavingProduct.objects.filter(kor_co_nm=bank_name).exists():
            savings = SavingProduct.objects.filter(kor_co_nm=bank_name)
            serializer = SavingListSerializer(savings, many=True)
            return Response(serializer.data)
        else:
            return Response({'detail': '해당 은행의 상품이 없습니다.'}, status=status.HTTP_204_NO_CONTENT)

# 개월 수에 해당하는 상품 + 원하는 기간의 옵션들 출력
# @api_view(['GET'])
# def deposit_month(request, month):
#     if request.method == 'GET':
#         deposits = DepositProduct.objects.filter(depositoption__save_trm=month).order_by('depositoption__intr_rate')
#         serializer = DepositMonthSerializer(deposits, many=True, save_trm=month)
#         return Response(serializer.data)


# @api_view(['GET'])
# def saving_month(request, month):
#     if request.method == 'GET':
#         savings = SavingProduct.objects.filter(savingoption__save_trm=month).order_by('savingoption__intr_rate')
#         serializer = SavingMonthSerializer(savings, many=True, save_trm=month)
#         return Response(serializer.data)

@api_view(['GET', 'POST'])
def like_deposit(request, deposit_code):
    deposit = get_object_or_404(DepositProduct, fin_prdt_cd=deposit_code)
    user = request.user
    print(user)
    print(user.deposit)
    if deposit in user.deposit.all():
        print(deposit.id)
        deposit.interest_user.remove(user)  # 이미 좋아요한 경우 좋아요 취소
        print(user.deposit)
        return Response({'status': 'unliked'}, status=status.HTTP_200_OK)
    else:
        print(deposit.id)
        deposit.interest_user.add(user)  # 좋아요 추가
        print(user.deposit)
        return Response({'status': 'liked'}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def like_saving(request, saving_code):
    saving = get_object_or_404(SavingProduct, fin_prdt_cd=saving_code)
    user = request.user
    if saving in user.saving.all():
        user.saving.remove(saving)  # 이미 좋아요한 경우 좋아요 취소
        return Response({'status': 'unliked'}, status=status.HTTP_200_OK)
    else:
        user.saving.add(saving)  # 좋아요 추가
        return Response({'status': 'liked'}, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def deposit_recommend(request):
    user = get_object_or_404(User, username=request.user.username)
    salary = int(user.salary)
    wealth = int(user.wealth)
    tendency = int(user.tendency)

    if not wealth or not salary:
        if not wealth:
            return Response({"message": "유저의 희망기간이 없습니다."})
        elif not salary:
            return Response({"message": "유저의 희망적금금액이 없습니다."})

    deposit = DepositProduct.objects.filter(
        Q(max_limit__gte = (salary + wealth) // 2) | Q(max_limit__isnull=True)
    )
    if len(deposit) >= 9:
        if 0 <= tendency < 3:
            deposit = deposit.filter(depositoption__save_trm__lte = 6)
        elif 3 <= tendency < 6:
            deposit = deposit.filter(depositoption__save_trm__lte = 12)
        elif 6 <= tendency < 9:
            deposit = deposit.filter(depositoption__save_trm__lte = 24)
        else:
            deposit = deposit.filter(depositoption__save_trm__lte = 36)
    else:
        deposit = deposit
    recommend = list(set(deposit.order_by("-depositoption__intr_rate")[:8]))
    serializer = DepositRecommendSerializer(recommend, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def saving_recommend(request):
    user = get_object_or_404(User, username=request.user.username)
    salary = int(user.salary)
    wealth = int(user.wealth)
    tendency = int(user.tendency)

    if not wealth or not salary:
        if not wealth:
            return Response({"message": "유저의 희망기간이 없습니다."})
        elif not salary:
            return Response({"message": "유저의 희망적금금액이 없습니다."})

    saving = SavingProduct.objects.filter(
        Q(max_limit__gte = (salary + wealth) // 2) | Q(max_limit__isnull=True)
    )

    if len(saving) >= 9:
        if 0 <= tendency < 3:
            saving = saving.filter(savingoption__save_trm__lte = 6)
        elif 3 <= tendency < 6:
            saving = saving.filter(savingoption__save_trm__lte = 12)
        elif 6 <= tendency < 9:
            saving = saving.filter(savingoption__save_trm__lte = 24)
        else:
            saving = saving.filter(savingoption__save_trm__lte = 36)
    else:
        saving = saving
    recommend = list(set(saving.order_by("savingoption__intr_rate")[:8]))
    serializer = SavingRecommendSerializer(recommend, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def deposit_recommend_second(request):
    user = get_object_or_404(User, username=request.user.username)
    age = user.age
    deposits = user.deposit.all()
    cnt_lst = [0] * 70
    users = User.objects.all()
    for user in users:
        if age // 10 == user.age // 10:
            deposits = user.deposit.all()
            for deposit in deposits:
                cnt_lst[int(deposit.id)] += 1
    # print(cnt_lst)
    cnt_tpl = []
    for value in range(len(cnt_lst)):
        cnt_tpl.append((cnt_lst[value], value))
    # print(cnt_tpl)
    cnt_tpl.sort(key= lambda x: -x[0])
    best = []
    for i in range(10):
        best.append(cnt_tpl[i][1])
    return Response(best)
    

@api_view(['GET'])
def saving_recommend_second(request):
    user = get_object_or_404(User, username=request.user.username)
    age = user.age
    savings = user.saving.all()
    cnt_lst = [0] * 70
    users = User.objects.all()
    for user in users:
        if age // 10 == user.age // 10:
            savings = user.saving.all()
            for saving in savings:
                cnt_lst[int(saving.id)] += 1
    # print(cnt_lst)
    cnt_tpl = []
    for value in range(len(cnt_lst)):
        cnt_tpl.append((cnt_lst[value], value))
    # print(cnt_tpl)
    cnt_tpl.sort(key= lambda x: -x[0])
    best = []
    for i in range(10):
        best.append(cnt_tpl[i][1])
    return Response(best)