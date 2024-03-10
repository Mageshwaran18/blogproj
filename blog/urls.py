from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostUpdateView, PostDeleteView

urlpatterns = [
    # path('', views.home, name="blog-home"),
    path('about/', views.about, name="blog-about"),

    path('', PostListView.as_view(), name="blog-home"),
    path('post-new/', views.createProfile, name="blog-new"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="blog-detail"),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name="blog-update"),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name="blog-delete")
]