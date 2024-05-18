from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
  path('get_deposit_products/', views.get_deposit_products),
  path('get_saving_products/', views.get_saving_products),
  
  path('deposit/', views.deposit_product_list),
  path('deposit/<str:deposit_code>/', views.deposit_detail),
  path('deposit/<str:deposit_code>/option/', views.deposit_option_list),
  path('deposit/<str:deposit_code>/option/<int:option_id>/', views.deposit_option_detail),
  path('deposit/<str:deposit_code>/interest/', views.deposit_interest),
  path('bank/deposit/<str:bank_name>/', views.bank_deposit),
  path('deposit/month/<int:month>/', views.deposit_month),
  path('deposit/12month/', views.deposit_month, { 'save_trm': 12 }),
  path('deposit/24month/', views.deposit_month, { 'save_trm': 24 }),
  path('deposit/36month/', views.deposit_month, { 'save_trm': 36 }),

  path('saving/', views.saving_product_list),
  path('saving/<str:saving_code>/', views.saving_detail),
  path('saving/<str:saving_code>/option/', views.saving_option_list),
  path('saving/<str:saving_code>/option/<str:option_id>/', views.saving_option_detail),
  path('saving/<str:saving_code>/interest/', views.saving_interest),
  path('bank/saving/<str:bank_name>/', views.bank_saving),
  path('saving/6month/', views.saving_month, { 'save_trm': 6 }),
  path('saving/12month/', views.saving_month, { 'save_trm': 12 }),
  path('saving/24month/', views.saving_month, { 'save_trm': 24 }),
  path('saving/36month/', views.saving_month, { 'save_trm': 36 }),



]
