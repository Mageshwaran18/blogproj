from django.urls import path
from . import views
from .views import *

urlpatterns = [
    # path('', views.home, name="blog-home"),
    path('about/', views.about, name="blog-about"),
    path('chat', views.chat_room, name='chat'),
    path('room', views.room, name='room'),
    path('send', views.send_message, name='send_message'),
    path('delete_message/<int:message_id>/', views.delete_message, name='delete_message'),


<<<<<<< HEAD
    path('home/', PostListView.as_view(), name="blog-home"),
    path('', first , name="first"),
    path('option/', option , name="option"),
    path('domains/', domains , name="domains"),
    path('post-new/', views.createProfile, name="blog-new"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="blog-detail"),
=======
    path('', PostListView.as_view(), name="blog-home"),
    path('post-new', views.createProfile, name="blog-new"),
    path('post/<int:pk>', PostDetailView.as_view(), name="blog-detail"),
>>>>>>> 40854cce8d8d30f62a34b09a2284071b83f936ef
    path('post/<int:pk>/update', PostUpdateView.as_view(), name="blog-update"),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name="blog-delete"),
    path('form/', form , name="form"),
]
