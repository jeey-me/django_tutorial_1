"""
URL configuration for django_tutor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from community.views import write, articleList
from community.views import viewDetail, index

urlpatterns = [
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8000/write/
    path('write/', write, name='write'), #path,view의 함수
    path('list/', articleList, name='list'), #path,view의 함수
    # http://127.0.0.1:8000/view_detail/1 -> 동적페이지 숫자바뀔 때마다 변함 <int:num>로 표현
    path('view_detail/<int:num>/', viewDetail, name ='view_detail'),
    # http://127.0.0.1:8000/
    path('', index, name='index')
]
