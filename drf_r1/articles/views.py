from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer

# list : 전체 객체 조회
# object : 단일 객체 조회
# 4xx : 클라이언트 에러
# 5xx : 서버 에러
# 404 : Not found
from django.shortcuts import get_object_or_404, get_list_or_404

# GET : 조회
# POST : 생성
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # 하나의 게시글도 조회가안되면 404 error
        articles = get_list_or_404(Article)
        # 다중 데이터(여러개 객체) 일때 : many=True
        serializer = ArticleListSerializer(articles, many=True)
        # 직렬화된 데이터를 json형식으로 Response
        return Response(serializer.data)

    elif request.method == 'POST':
        # request.data : title, content
        print(request.data)
        serializer = ArticleSerializer(data=request.data)
        # raise_exception=True : 유효하지 않을경우 예외 발생
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # 데이터 생성에 성공/실패 -> 성공 HTTP_201, 실패 HTTP_400
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# GET : 조회, DELETE:삭제, PUT:수정
@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # get_object_or_404 : 객체가 조회안되면 404
    article = get_object_or_404(Article, pk=article_pk)
    # 단일 게시글 조회
    if request.method == 'GET': 
        # 직렬화 -> 응답
         serializer = ArticleSerializer(article)
         return Response(serializer.data)
    # 게시글 삭제
    elif request.method == 'DELETE':
        article.delete()
        # HTTP_204_NO_CONTENT : 요청 성공, 반환할 콘텐츠가 없다
        return Response(status=status.HTTP_204_NO_CONTENT)
    # 게시글 수정
    elif request.method == 'PUT':
        # partial=True : 부분 업데이트 허용(일부 필드만 수정 가능)
        serializer = ArticleSerializer(
            article, data=request.data, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET'])
def comment_list(request):
    # 댓글 하나도 없으면 404에러
    comments = get_list_or_404(Comment)
    # 직렬화 하고 응답
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # 댓글부터 조회
    comment = get_object_or_404(Comment, pk=comment_pk)
    # 조회
    if request.method == 'GET': 
        # 직렬화 -> json으로 응답
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    # 삭제
    if request.method == 'DELETE': 
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # 수정
    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        # 유효성 검사
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
@api_view(['POST'])
def comment_create(request, article_pk):
    # 게시글부터 조회
    article = get_object_or_404(Article, pk=article_pk)

    serializer = CommentSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
