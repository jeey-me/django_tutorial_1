from django.contrib import admin
from django.urls import path
from community.views import write, articleList
from community.views import viewDetail

urlpatterns = [
    # http://127.0.0.1:8000/write/
    path('write/', write, name='write'), #path,view의 함수
    path('list/', articleList, name='list'), #path,view의 함수
    path('view_detail/<int:num>/', viewDetail, name ='view_detail'),
]

