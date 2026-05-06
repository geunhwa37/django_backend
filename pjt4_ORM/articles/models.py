from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model() # 간접 참조

# Create your models here.
class Article(models.Model):
    # settings.py의 AUTH_USER_MODEL
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # 역참조 했을 때
    # User가 작성한 게시글 역참조 : user.article_set
    # User가 좋아요 누를 게시글 역참조: user.like_articles
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='like_articles'
    )

    title = models.CharField(max_length=20)
    content = models.TextField()
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    # 게시글과 댓글 간의 관계 (Many-to-one) 
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)