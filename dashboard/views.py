from django.shortcuts import render, redirect
from dashboard.forms import CountryDataForm
from dashboard.models import CountryData

def dashboard(request): 
    datas = CountryData.objects.all()

    if request.method == 'POST':
        form = CountryDataForm(request.POST)
        if form.is_valid():
            country = form.cleaned_data.get('country')
            population = form.cleaned_data.get('population')

            # 기존 국가 있는지 확인
            existing = CountryData.objects.filter(country=country).first()
            if existing:
                if existing.population != population:
                    existing.population = population  # 업데이트
                    existing.save()
                    print(f"{country} 인구수 업데이트 완료")
                else:
                    print(f"{country} 인구수 동일 - 저장 생략")
            else:
                form.save()  # 새로운 국가면 저장
                print(f"{country} 새로 저장됨")
            return redirect("/dashboard")
    else:
        form = CountryDataForm()

    context = {
        'dataset': datas,
        'form': form,
    }
    return render(request, 'dashboard.html', context)
