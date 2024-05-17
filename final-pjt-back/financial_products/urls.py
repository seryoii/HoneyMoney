from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
  path('get_deposit_products/', views.get_deposit_products),
  path('get_saving_products/', views.get_saving_products),
  path('deposit_list/', views.deposit_product_list),
  path('saving_list/', views.saving_product_list),
]
