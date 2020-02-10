"""pawnwalkerwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,re_path
from dogowner.views import *
from dogwalker.views import *
import dogowner.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dogowner.views.index, name='index'),
    re_path(r'dogowner/register/$', registerUser,name='dogowner_register_view'),
    re_path(r'dogwaler/register/$', registerUserDogWalker,name='dogwalker_register_view'),
    re_path(r'dogowner/login/$', loginUser,name='dogowner_login_view'),
    re_path(r'dogwalker/login/$', loginUserDogWalker,name='dogwalker_login_view'),


]
