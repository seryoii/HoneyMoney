from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
# 초기 상품 데이터 생성하기
  path('get_deposit_products/', views.get_deposit_products),
  path('get_saving_products/', views.get_saving_products),
  
# deposit
  path('deposit/', views.deposit_product_list),
  path('deposit/<str:deposit_name>/', views.deposit_detail),
  path('deposit/<str:deposit_code>/option/', views.deposit_option_list),
  path('deposit/<str:deposit_code>/option/<int:option_id>/', views.deposit_option_detail),
  # path('deposit/<str:deposit_code>/interest/', views.deposit_interest),
  path('bank/deposit/<str:bank_name>/', views.bank_deposit),
  # path('deposit/month/<int:month>/', views.deposit_month),
  path('like/deposit/<str:deposit_code>/', views.like_deposit),
  path('recommend/deposit/<str:username>/', views.deposit_recommend),
  # 나이로 상품 추천 (반환 값: 상품 데이터의 id 값)
  path('recommend/deposit/second/', views.deposit_recommend_second),

# saving
  path('saving/', views.saving_product_list),
  path('saving/<str:saving_name>/', views.saving_detail),
  path('saving/<str:saving_name>/option/', views.saving_option_list),
  path('saving/<str:saving_code>/option/<str:option_id>/', views.saving_option_detail),
  # path('saving/<str:saving_code>/interest/', views.saving_interest),
  path('bank/saving/<str:bank_name>/', views.bank_saving),
  # path('saving/month/<int:month>/', views.saving_month),
  path('like/saving/<str:saving_code>/', views.like_saving),
  path('recommend/saving/', views.saving_recommend),
  # 나이로 상품 추천 (반환 값: 상품 데이터의 id 값)
  path('recommend/saving/second/', views.saving_recommend_second),



]
