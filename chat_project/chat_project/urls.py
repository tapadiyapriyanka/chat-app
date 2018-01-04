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
from .views import json_web_token_auth, RegistrationView, LoginView
from .forms import LoginForm
# from rest_framework_jwt.views import obtain_jwt_token

# from .views import RegistrationView, LoginView
from home import urls as home_urls
from chat_app import urls as chat_urls

admin.autodiscover()

urlpatterns =[
    url(r'', include(home_urls, namespace='auth')),
    url(r'^chat/', include(chat_urls, namespace='chat')),
    # url(r'^goal/', include('goal.urls', namespace='goal')),
    # url(r'', include('home.urls', namespace='home')),

    # url(r'^api/auth/register/', RegistrationView.as_view(), name='register'),
    # url(r'^api/auth/login/', LoginView.as_view(), name='login'),
    # url(r'^api/home/', include(home_urls)),

    url(r'^admin/', admin.site.urls),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^login/$', login, {'template_name': 'registration/login.html', 'authentication_form': LoginForm}, name='login_form'),
    # # url(r'^token/', json_web_token_auth, name='authenticate'),
    # url(r'^logout/', logout, name='logout'),  # The base django logout view
    # # url(r'^logout/$', logout, {'next_page': '/login'}, name='logout'),
    # # url(r'^logout_redirect/', views.logout_method, name='logout_redirect'),
    # url(r'^signup/', views.signup, name='signup'),
    # # # url(r'^admin/', admin.site.urls, name='adminpage'),
    # url(r'^chat/', include('chat_app.urls')),
    # url('', views.homePageView.as_view(), name='homepage')
]

# urlpatterns += [
#     url(r'^api/auth/register/', RegistrationView.as_view(), name='register'),
#     url(r'^api/auth/login/', LoginView.as_view(), name='login'),
#     url(r'^api/home/', include(home_urls))
# ]
