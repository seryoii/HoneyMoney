from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
  path('get_deposit_products/', views.get_deposit_products),
  path('get_saving_products/', views.get_saving_products),
]
