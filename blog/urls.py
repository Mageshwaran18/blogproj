from django.urls import path
from . import views
from .views import *

urlpatterns = [
    # path('', views.home, name="blog-home"),
    path('about/', views.about, name="blog-about"),

    path('home/', PostListView.as_view(), name="blog-home"),
    path('', first , name="first"),
    path('option/', option , name="option"),
    path('domains/', domains , name="domains"),
    path('post-new/', views.createProfile, name="blog-new"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="blog-detail"),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name="blog-update"),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name="blog-delete"),
    path('form/', form , name="form"),
]
