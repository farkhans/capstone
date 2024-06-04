from django.urls import path
from .views import GetArticles, CreateArticle

app_name = 'article'

urlpatterns = [
    path('get-articles', GetArticles.as_view(), name='get_articles'),
    path('create-article', CreateArticle.as_view(), name='create_article'),
]