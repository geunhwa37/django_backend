from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'), # 회원가입
    path('delete/', views.delete, name='delete'), # 회원탈퇴
    path('update/', views.update, name='update'), # 회원정보변경
    path('password/', views.change_password, name='change_password')
]
