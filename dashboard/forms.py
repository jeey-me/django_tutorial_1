# html 입력데이터 db저장을 위한 forms.py 생성
from django.forms import ModelForm
from .models import CountryData

class CountryDataForm(ModelForm):
    class Meta:
        model = CountryData
        fields = '__all__'