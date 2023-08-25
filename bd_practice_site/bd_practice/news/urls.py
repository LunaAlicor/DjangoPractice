from django.urls import path
from . import views


urlpatterns = [
    path('', views.news, name='news'),
    path('<int:pk>', views.NewsDetail.as_view(), name='news-detail'),
    path('search/', views.search_results, name='search_results'),
]
