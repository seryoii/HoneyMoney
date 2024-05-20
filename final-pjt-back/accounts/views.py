from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import UserPageSerializer, UserInfoChangeSerializer, UserGetInterestSerializer
from .models import User

# Create your views here.

@api_view(['GET', 'PUT'])
def mypage(request, username):
    if request.user.username != username:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        if request.user.username == username:
            user = get_object_or_404(get_user_model(), username=username)
            serializer = UserInfoChangeSerializer(user)
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

# def sync_deposit_interest_users(request):
#     # 현재 로그인된 사용자
#     user = request.user

#     try:
#         # 사용자 deposit 필드에서 모든 DepositProduct ID 가져오기
#         deposit_ids = user.deposit.values_list('id', flat=True)

#         # 각 DepositProduct의 interest_user에 사용자 추가
#         for deposit_id in deposit_ids:
#             deposit_product = get_object_or_404(DepositProduct, id=deposit_id)
#             deposit_product.interest_user.add(user)

#         # 사용자의 갱신된 정보 직렬화
#         serializer = UserPageSerializer(user)

#         return JsonResponse({'status': 'success', 'message': 'Deposit interest users synchronized successfully', 'data': serializer.data})
#     except Exception as e:
#         return JsonResponse({'status': 'error', 'message': str(e)})
@api_view(['GET'])
def get_interest(request):
    users = User.objects.all()
    for user in users:
        print(user.deposit)
    serializer = UserGetInterestSerializer(users, many=True)
    return Response(serializer.data)
    # for user in users:
    #     print(user.deposit)
