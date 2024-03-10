from django.urls import path
from .views import *

urlpatterns =[
    path('logout/',custom_logout,name='logout'),
    path('logoutt/',logout_form,name='logoutt')
]