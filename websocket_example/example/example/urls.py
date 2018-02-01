"""example URL Configuration

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
from django.contrib import admin
# from django.urls import path,include
# from django.conf.urls import url, include
from django.conf.urls import *
from websocket_app.views import user_list,login, log_out, sign_up

app_name = "websocket_app"

urlpatterns = [
    url('admin/', admin.site.urls),
    # url(r'^', user_list, name='userlist'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', log_out, name='logout'),
    url(r'^signup/$', sign_up, name='signup'),
    url(r'^', user_list, name='userlist')
]
