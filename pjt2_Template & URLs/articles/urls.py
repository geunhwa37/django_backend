from django.contrib import admin
from django.urls import path
from . import views

# 다른 앱과 혼동하지 않기 위해서
# url naming pattern에 쓰임 
app_name = 'articles' 

urlpatterns = [
    # views.py의 index 함수를 실행하겠다 
    # html에서 href="/index/" 이렇게 url을 하드코딩 하지 않을거다
    # name = "index" -> named url patterns
    # {% url 'articles:index' %}
    path('index/', views.index, name = "index"),
    path('dinner/', views.dinner, name = "dinner"),
    path('search/', views.search, name = "search"),
    path('throw/', views.throw, name ="throw"),
    path('catch/', views.catch, name ="catch"),
    # variable routing = 여러개의 url(숫자만 다른)을 하나의 뷰로 처리
    # <데이터 타입:변수명>
    path('<int:number>/', views.detail, name ="detail"),
]
