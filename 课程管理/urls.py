"""
URL configuration for 课程管理 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# 课程管理/urls.py

from django.contrib import admin
from django.urls import path, include
from courses import views

#urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('课程/', include('courses.urls')),
    #path('', views.课程列表, name='主页'),  # 根URL映射到课程列表视图
#]
#urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', include('courses.urls')),
#]

#urlpatterns = [
    #path('courses/', include('courses.urls')),
#]

urlpatterns = [
    path('', views.index, name='index'),
]
