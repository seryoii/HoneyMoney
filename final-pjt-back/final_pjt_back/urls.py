"""
URL configuration for final_pjt_back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # settings를 가져옵니다.
from django.conf.urls.static import static  # static을 가져옵니다.

urlpatterns = [
    path('admin/', admin.site.urls),
    # TokenAuthentication
     path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # Registration 
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('accounts/', include('accounts.urls')),
    path('articles/', include('articles.urls')),
    path('exchange/', include('exchange.urls')),
    path('products/', include('financial_products.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)