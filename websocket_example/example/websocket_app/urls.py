from django.conf.urls import url
from websocket_app.views import user_list,login, log_out, sign_up

app_name = "websocket_app"

urlpatterns=[
    url(r'^$', user_list, name='user_list'),
]
