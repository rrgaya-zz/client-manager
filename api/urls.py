from django.urls import path
from .views import ArticleView, PostList, PostDetail


app_name = "articles"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path('articles/<int:pk>', ArticleView.as_view()),
    path('articles/<int:pk>', ArticleView.as_view()),
    path('articles/<int:pk>', ArticleView.as_view()),
]