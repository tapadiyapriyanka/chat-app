from django.conf.urls import *
from . import views
# from chat_app.views import user_data
# from rest_framework.routers import SimpleRouter
#
# from .views import SubscriberView
#
# router = SimpleRouter()
# router.register("subscribers", SubscriberView)
#
# urlpatterns = router.urls


# from rest_framework.routers import SimpleRouter
#
# from .views import SubscriberView
#
# router = SimpleRouter()
# router.register("subscribers", SubscriberView)
# print(router.urls)
# # urlpatterns = [
#     # router.urls
# # ]
app_name = "chat_app"

urlpatterns = [
    # url(r'^subscriber', SubscriberView.as_view(), name="subscriber")
    # url('list/', SubscriberView.as_view(), name = 'home'),      #views.chatListView
    url('list/', views.chatListView.as_view(), name='chat_home'),      #views.chatListView
    url('detail/<int:pk>', views.chatDetailView.as_view(), name = 'chat_detail'),
    url('edit/<int:pk>', views.chatUpdateView.as_view(), name='chat_edit'),
    url('delete/<int:pk>',views.chatDeleteView.as_view(), name='chat_delete'),
    url('edit_delete', views.chatEditdeleteView.as_view(), name='edit_delete'),
    
]
