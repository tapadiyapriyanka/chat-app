from django.conf.urls import *
import home.views as views

app_name = 'home'

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^logout/$', views.Logout.as_view(), name='logout'),
]
