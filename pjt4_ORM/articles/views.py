from django.shortcuts import render, redirect

# Create your views here.
from .models import Article, Comment
from .forms import CommentForm

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

# 전체 데이터 조회 
def index(request):
    # QuerySet API : Article.objects.all()
    articles = Article.objects.all()
    
    context = {
        'articles':articles
    }

    return render(request, 'articles/index.html', context)

@require_http_methods(['GET'])
def detail(request, pk):
    # QuerySet API ---> 단일 게시글 조회: get
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()

    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }

    return render(request, 'articles/detail.html', context)

from .forms import ArticleForm

#  create
# 페이지 렌더링 + 리다이렉트(if-else 구조)
@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    # submit 버튼 눌렀을 때
    if request.method == "POST":
        # 파일은 따로 관리, request.FILES - image, file 등
        form = ArticleForm(request.POST, request.FILES)
        # 1. 모든 필수 필드가 채워져 있는지
        # 2. 입력된 데이터가 필드 조건을 만족하는지(데이터 타입, 길이 제한)
        if form.is_valid():
            article = form.save(commit=False)
            # request.user = 로그인한 유저
            article.user = request.user
            # DB에 저장
            article.save()

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
@login_required
@require_http_methods(['GET', 'POST'])
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
@login_required
@require_http_methods(['POST'])
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()

    return redirect('articles:index')

# 댓글 생성
@login_required
@require_http_methods(['POST'])
def comments_create(request, pk):
    # 게시글 조회
    article = Article.objects.get(pk=pk)
    comments_form = CommentForm(request.POST)

    # 유효성 검사
    if comments_form.is_valid():
    # commit=False : DB에 바로 저장 X
        comment = comments_form.save(commit=False)
        comment.article = article # 1. 게시글 객체
        comment.user = request.user # 2. 로그인한 user
        comment.save() # DB에 저장

        return redirect('articles:detail', article.pk)

    # 유효성 검사 실패
    context = {
        'article': article,
        'comments_form': comments_form,
        
    }
    return render(request, 'articles:detail.html', context)

# 댓글 삭제
@login_required
@require_http_methods(['POST'])
def comments_delete(request, article_pk, comment_pk):
    # 댓글 조회
    comment = Comment.objects.get(pk=comment_pk)

    # 로그인한 USER == 댓글 작성한 USER
    if request.user == comment.user:
        comment.delete()    

    return redirect('articles:detail', article_pk)