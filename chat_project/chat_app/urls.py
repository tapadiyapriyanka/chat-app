from django.urls import path
from . import views

urlpatterns = [
    path('chat/list/', views.chatListView, name = 'home'),
    path('chat/<int:pk>/', views.chatDetailView.as_view(), name = 'chat_detail'),
    # path('chat/new/', views.chatCreateView.as_view(), name="chat_new"),
    path('chat/<int:pk>/edit/', views.chatUpdateView.as_view(), name='chat_edit'),
    path('chat/<int:pk>/delete/',views.chatDeleteView.as_view(), name='chat_delete'),
    path('chat/edit_delete', views.chatEditdeleteView.as_view(), name='edit_delete'),
]
