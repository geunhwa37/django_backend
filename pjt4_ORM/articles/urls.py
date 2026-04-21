"""
URL configuration for CRUD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name="index"), # read

    # variable routing
    path('<int:pk>/', views.detail, name = 'detail'),
    
    # # 왜 url을 2개로 나눴을까? 
    # path('new/', views.new, name = 'new'), # 페이지 렌더링
    # path('create/', views.create, name = 'create'), # 페이지 리다이렉트
    path('create/', views.create, name = 'create'),

    # path('<int:pk>/edit/', views.edit, name = 'edit'), # 페이지 렌더링
    # path('<int:pk>/update/', views.update, name = 'update'), # 페이지 리다이렉트
    path('<int:pk>/update/', views.update, name = 'update'),

    path('<int:pk>/delete/', views.delete, name = 'delete')
    
]
