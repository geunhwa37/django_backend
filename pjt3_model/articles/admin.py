from django.contrib import admin

# Register your models here.
from .models import Articles

# 어드민 사이트에 등록하겠다
admin.site.register(Articles)