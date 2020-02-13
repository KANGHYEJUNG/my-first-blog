from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'), # 상세 페이지 url 만들기
    path('post/new', views.post_new, name='post_new'), # 새 게시글 추가하기
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'), # 특정 게시글 수정하기
]

