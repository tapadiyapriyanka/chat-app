from django.conf.urls import *
import home.views as views
# from chat_app import views as chat_view
from django.contrib import admin
app_name = 'home'

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^logout/$', views.Logout.as_view(), name='logout'),
    url('admin/', admin.site.urls),
    url('user_data/', views.user_data, name='user_data'),
    url('signup/', views.sign_up, name='sign_up'),
]
