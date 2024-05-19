from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
    path('<str:username>/', views.mypage),
    path('profile/<str:username>/', views.user_profile),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
