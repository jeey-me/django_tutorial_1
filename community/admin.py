from django.contrib import admin
from .models import Article  # models.py에서 Article 모델 가져오기

# Article 모델을 관리자 페이지에 등록
admin.site.register(Article)

