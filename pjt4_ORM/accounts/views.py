from django.shortcuts import render, redirect

from django.contrib.auth.forms import(
    AuthenticationForm, # 로그인을 위한 폼(id, password 입력)
    PasswordChangeForm # 비밀번호 변경 폼(현재 비밀번호, 변경할 비밀번호)
)
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from .models import User

from django.contrib.auth.decorators import login_required # 로그인 하지 않은 상태에서 url 접근하는 것을 방지


def login(request):
    # 로그인 버튼 눌렀을 때(로그인 Url로 접근했을 때)
    if request.method == 'POST':
        # request.POST : 사용자가 입력한 ID, Password
        form = AuthenticationForm(request, request.POST)
        if form.is_valid(): # 유효성 검사 통과하면 로그인 처리
            # get_user() : 인증된 사용자의 객체 반환
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else: # 로그인 버튼을 누르기 전
        form = AuthenticationForm() # 빈 폼
    # GET 요청 or 유효성 검사 실패 시
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)

    # 로그인, 로그아웃 다 POST 요청
    return redirect('articles:index')

from .forms import CustomUserCreationForm, CustomUserChangeForm

def signup(request):
    # 상황 - 이미 로그인하고, 회원가입 페이지로 이동하려고 할 때 
    if request.user.is_authenticated:  # is_authenticated 속성 : 이미 인증된 사용자라면
        return redirect('articles:index')
    
    # 상황 - 필수 입력 다 하고, 회원가입 완료 버튼 눌렀을 때
    if request.method == 'POST': 
        # request.POST - 우리가 회원가입 페이지에서 입력한 것들 
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():  # 1. 유효성 검사
            user = form.save()  # 2. 디비에 저장
            auth_login(request, user) # 3. 로그인

            return redirect('articles:index')
    else: 
        form = CustomUserCreationForm() # 빈 폼
    # GET 요청(회원가입 페이지) or 유효성 검사 실패 시
    context = {
        'form' : form
    }

    return render(request, 'accounts/signup.html', context)

@login_required
def delete(request):
    # request.user : 현재 로그인 되어있는 user
    request.user.delete()
    return redirect('articles:index')

@login_required
def update(request):
    # 회원정보변경완료 버튼을 눌렀을때
    if request.method == "POST":
        # request.POST : 내가 입력할 필드의 값들
        # instance : 기존의 db에 저장되어있던 값들 가져옴
        # request.user : 로그인한 user
        form = CustomUserChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else: # POST 요청이 아닐때
        form = CustomUserChangeForm(instance = request.user)

    # GET 요청 or 유효성검사 실패했을 때
    context = {
        'form' : form
    }

    return render(request, 'accounts/update', context)

@login_required
def change_password(request):
    if request.method == "POST":
        # 첫 번째 인자는 user, 두 번째 인자는 입력한 데이터
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # 세션 무효화 방지(자동 로그아웃 방지)
            # hash 함수로 현재 사용자의 인증 세션 갱신
            update_session_auth_hash(request, user)
            return redirect('articles:index.html')
    else:
        form = PasswordChangeForm(request.user)
    
    context = {
        'form' : form
    }

    return render(request, 'accounts/change_password.html', context)