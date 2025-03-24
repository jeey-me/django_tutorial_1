from django.shortcuts import render
from dashboard.models import CountryData
# Create your views here.


def dashboard(request) : 
    # 비즈니스 로직
    # db 테이블에서 데이터 조회 
    datas = CountryData.objects.all()
    #랜더링 데이터 만들기 
    context = {
        'dataset': datas
    }
    return render(request, 'dashboard.html', 
                  context)