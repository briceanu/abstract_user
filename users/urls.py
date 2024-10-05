

from django.urls import path
from .views import BlogAbstractUserApiView



urlpatterns =[
    path('signup', BlogAbstractUserApiView.as_view(), name='signup')]