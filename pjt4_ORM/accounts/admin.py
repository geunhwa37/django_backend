from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# models.py의 User 모델을 가져옴
from .models import User

# admin 사이트에 등록하겠다 (User 모델, UserAdmin)
admin.site.register(User, UserAdmin)