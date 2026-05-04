from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

# User 모델 직접 참조
# from .models import User

# 간접 참조
# get_user_model  ---> AbstractUser 간접참조 함수
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model() # 간접 참조

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model() # 간접 참조
        # user가 회원정보 변경할 필드만 가져오기
        fields = ('first_name', 'last_name', 'email', )