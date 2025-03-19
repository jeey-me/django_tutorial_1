from django.shortcuts import render
from community.forms import Form
from .models import Article  # 현재 앱(community)의 models.py에서 import
# Create your views here.


def write(request) :
    # 비즈니스 로직 구현
    hello = "안녕 장고"
    form = Form()
    return render(request, 'write.html', {'hello_django': hello, 'form':form})

def write(request) :
    # 사용자 요청 method가 Post일때 
    if request.method == 'POST':
        # request.post 데이터를폼객체로 생성
        form = Form(request.POST)
        # print(from)
        if form. is_valid():
            form.save() # 필드값 저장함수
    else:
        form =Form()
    return render(request, 'write.html', {'form':form}) #request, template,

def articleList(request) : 
    article_list = Article.objects.all()
    # print(article_list)
    # for a in article_list : 
    #     print("이름: ", a.name, "제목 : ", a.title)
     # return render(request, '/index.html',{'키' : 파이썬변수})
    return render(request, 'list.html', {'article_list': article_list})

# 글 상세보기 뷰 함수
def viewDetail(request, num=1):
    Article_detail = Article.objects.get(id=num)
   # Article_detail = get_object_or_404(Article, id =num)
    return render(request, 'view_detail.html', {'article_detail': Article_detail})

def index(request) : 
    latest_article_list = Article.objects.all().order_by('-cdate')[:3]
    return render(request, 'index.html',{'latest_article_list': latest_article_list})
# 인덱스 페이지에 최근 목록 3 개 보이도록 하고 ,
# 버튼을 누르면 메모 작성하기로 가도록 구현


