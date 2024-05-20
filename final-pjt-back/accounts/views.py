from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import UserPageSerializer, UserInfoChangeSerializer, UserGetInterestSerializer, NewInfoChangeSerializer
from .models import User
from financial_products.models import DepositProduct, SavingProduct

# Create your views here.

@api_view(['GET', 'PUT'])
def mypage(request, username):
    # if request.user.username != username:
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        # if request.user.username == username:
        user = get_object_or_404(get_user_model(), username=username)
        serializer = NewInfoChangeSerializer(user)
        return Response(serializer.data)
        
    elif request.method == 'PUT':
        if request.user.username == username:
            user = get_object_or_404(get_user_model(), username=username)
            # data = { 'profile_img': request.data['profile_img[]']}

            serializer = UserInfoChangeSerializer(instance=user, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def user_profile(request, username):
    # 관리자 또는 자신의 프로필에만 접근 가능
    print('가', username)
    print('나', request.user)
    if request.user.username != username:
        return Response({"error": "You are not authorized to view this profile."}, status=status.HTTP_403_FORBIDDEN)

    user = get_object_or_404(get_user_model(), username=username)
    # profile_img_url = request.build_absolute_uri(user.profile_img.url)

    serializer = UserPageSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

# 더미 데이터의 deposit, saving 기반으로 상품에 관심있는 테이블 생성
@api_view(['GET'])
def get_interest(request):
# 유저 객체 가져오기
    for user_id in range(1, 10001):
        user = get_object_or_404(User, id=user_id)

        # 유저의 deposit 필드 값 가져오기
        deposit_ids = user.deposit.all().values_list('id', flat=True)
        saving_ids = user.saving.all().values_list('id', flat=True)

        # deposit_ids와 매칭되는 DepositProduct 모델의 객체들의 interest_user 필드에 유저 id 할당하기
        for deposit_id in deposit_ids:
            deposit_product = get_object_or_404(DepositProduct, id=deposit_id)
            deposit_product.interest_user.add(user)
        for saving_id in saving_ids:
            saving_product = get_object_or_404(SavingProduct, id=saving_id)
            saving_product.interest_user.add(user)

    return JsonResponse({'message': 'Successfully assigned interest users to deposit, saving products'})

def personal_interest(request, user_id):
    user = User.objects.get(id=user_id)
    user_ids = user.interest_deposit.all()
    for deposit_product in user_ids:
        print(deposit_product.id)    
    return JsonResponse({'message': 'success'})
    # objects.filter(depositproduct_id=depositproduct_id).values_list('user_id', flat=True)

