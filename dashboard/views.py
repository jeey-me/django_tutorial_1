from django.shortcuts import render
# Create your views here.


def dashboard(request) : 
    
    # print(article_list)
    # for a in article_list : 
    #     print("이름: ", a.name, "제목 : ", a.title)
     # return render(request, '/index.html',{'키' : 파이썬변수})
    return render(request, 'dashboard.html',)