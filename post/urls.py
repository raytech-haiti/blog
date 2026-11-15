from django.urls import path
from post.views import HomePageView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = 'post'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('<str:slug>/', ArticleDetailView.as_view(), name='article'),
    path('update/<str:slug>/', ArticleUpdateView.as_view(), name='update'),
    path('delete/<str:slug>/', ArticleDeleteView.as_view(), name='delete'),
]