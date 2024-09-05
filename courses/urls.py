# courses/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.课程列表, name='课程列表'),
    path('学生管理/', views.学生管理, name='学生管理'),
    path('课程管理/', views.课程管理, name='课程管理'),
    path('收入管理/', views.收入管理, name='收入管理'),
    path('费用管理/', views.费用管理, name='费用管理'),
]