from django.urls import path

from hexlet_django_blog.article import views

urlpatterns = [
    path('', views.ArticlePageView.as_view(), name='articles'),
    path('<str:tag>/<int:article_id>', views.ArticlePageView.as_view(), name='article')
]