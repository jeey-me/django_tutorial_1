from django.shortcuts import render
from community.models import Article


def index(request) : 
    latest_article_list = Article.objects.all().order_by('-cdate')[:3]
    return render(request, 'index.html',{'latest_article_list': latest_article_list})
# 인덱스 페이지에 최근 목록 3 개 보이도록 하고 ,
# 버튼을 누르면 메모 작성하기로 가도록 구현