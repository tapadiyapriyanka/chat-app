"""chat_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import *
from django.contrib import admin

from django.contrib.auth.views import login, logout
from chat_app import views
from .views import json_web_token_auth

admin.autodiscover()

urlpatterns =[
    url(r'^login/', login, name='login'),  # The base django login view
    url(r'^token/', json_web_token_auth, name='authenticate'),
    url(r'^logout/', logout, name='logout'),  # The base django logout view
    url(r'^logout_redirect/', views.logout_method, name='logout_redirect'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^admin/', admin.site.urls, name='adminpage'),
    url(r'^chat/', include('chat_app.urls')),
    url('', views.homePageView.as_view(), name='homepage')
]
