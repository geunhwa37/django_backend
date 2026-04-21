from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'name': 'Bogeom',
        'number': 3
    }

    # render의 3번째 인자는 context
    # templates의 articles의 index.html로 context를 넘겨주겠다
    return render(request, 'articles/index.html', context)

import random

def dinner(request):
    foods = ['족발', '보쌈', '치킨', '피자']
    picked = random.choice(foods)
    context = {
        'foods': foods,
        'picked': picked
    }
    return render(request, 'articles/dinner.html', context)

def search(request):
    return render(request, 'articles/search.html')

def throw(request):

    # throw 페이지에서 form 태그로 던질거다.
    return render(request, 'articles/throw.html')

def catch(request):

    # name이 뭘까???가 중요하다
    # name="throw"
    text = request.GET.get('throw') # 이 get은 딕셔너리 메서드

    context = {
        'text': text
    }

    return render(request, 'articles/catch.html', context)

def detail(request, number):
    context = {
        'number': number
    }
    return render(request, 'articles/detail.html', context)