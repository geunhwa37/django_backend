from django.shortcuts import render, redirect

# Create your views here.
from .models import Article

# 전체 데이터 조회
def index(request):
    # QuerySet API : Article.objects.all()
    articles = Article.objects.all()
    
    context = {
        'articles':articles
    }

    return render(request, 'articles/index.html', context)

def detail(request, pk):
    # QuerySet API ---> 단일 게시글 조회: get
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }

    return render(request, 'articles/detail.html', context)

from .forms import ArticleForm

#  create
# 페이지 렌더링 + 리다이렉트(if-else 구조)
def create(request):
    # submit 버튼 눌렀을 때
    if request.method == "POST":
        # 파일은 따로 관리, request.FILES - image, file 등
        form = ArticleForm(request.POST, request.FILES)
        # 1. 모든 필수 필드가 채워져 있는지
        # 2. 입력된 데이터가 필드 조건을 만족하는지(데이터 타입, 길이 제한)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else: # submit 버튼 누르기 전, 다른 버튼(다른 요청일 때)
        form = ArticleForm() # 빈 폼
    
    # GET 요청
    context = {
        'form': form
    }
    return render(request, 'articles/create.html', context)
 
# # 페이지 렌더링(GET 요청)
# def new(request):
#     return render(request, 'articles/new.html')

# # 페이지 리다이렉트(POST 요청)
# def create(request):
#     title = request.POST.get('title') # html 폼태그에서 name으로 온 title
#     content = request.POST.get('content')

#     article = Article(title = title, content = content)
#     article.save()

#     return redirect('articles:detail', article.pk)

# # 페이지 렌더링
# # 기존에 있던 게시글을 조회
# def edit(request, pk):
#     article = Article.objects.get(pk=pk)

#     context = {
#         'article': article
#     }

#     return render(request, 'articles/edit.html', context)

# # 기존에 있던 게시글을 변경 (db 레코드 변경)
# def update(request, pk):
#     article = Article.objects.get(pk=pk)

#     # 기존의 article을 변경 
#     article.title = request.POST.get('title')
#     article.content = request.POST.get('content')
#     article.save()

#     return redirect('articles:detail', article.pk)

# 수정
def update(request, pk):
    article = Article.objects.get(pk=pk)

    # submit 버튼 눌렀을 때
    if request.method == "POST":
        # 기존 게시글의 데이터를 미리 채운다(instance = article)
        form = ArticleForm(request.POST, request.FILES, instance = article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else: # GET 요청일 때, (POST 요청이 아닐 때)
        form = ArticleForm(instance=article)

    context = {
        'article': article,
        'form': form
    }

    return render(request, 'articles/update.html', context)

 
 # 단일 게시글 조회 후 삭제
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()

    return redirect('articles:index')

