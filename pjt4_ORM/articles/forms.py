from django import forms
from .models import Article

# form 태그 사용해서 name으로 넘겨주고 DB에 저장 가능
# 단, 로직을 수동으로 구현해줘야 함
# ModelForm은 form.save()하면 바로 DB에 저장
# 왜 쓸까? 편의성 + 유효성 검사에 용이함
class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        # fields = ('title', 'content', 'created_at', 'updated_at', )
        fields = '__all__'
