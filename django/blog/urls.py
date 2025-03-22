from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.blog_post, name='blog_post'),
    path('comment/', views.blog_comment, name='blog_comment'),
]