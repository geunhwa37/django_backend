from django.db import models

# AbstractUser : User 관련된 기본적인 필드를 제공
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    followings = models.ManyToManyField(
        'self', symmetrical=False, related_name='followers' # symmetrical=False : 내가 상대방을 팔로잉 했다고, 상대방이 나를 팔로우 한 건 아니다.

    )