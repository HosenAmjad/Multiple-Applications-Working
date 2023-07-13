"""applications URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.urls import path, include
from django.urls.conf import include
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('userlogin', views.userlogin.as_view(), name='userlogin'),
    path('userlogout', views.userlogout.as_view(), name='userlogout'),
    path('signup', views.signup.as_view(), name='signup'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('deshboard', views.deshboards.as_view(), name='deshboard'),
    path('terms', views.terms.as_view(), name='terms'),
    path('helps', views.helps.as_view(), name='helps'),
    path('privace', views.privace.as_view(), name='privace'),
]
