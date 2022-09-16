from django.urls import path, include
from django.contrib import admin
from .views import *


urlpatterns = [
    #path('', index, name='home'),Z
    path('', HomeNews.as_view(), name='home'),
    #path('category/<int:category_id>/', get_category, name='category'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    #path('news/<int:news_id>/', view_news, name='view_news'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    #path('news/add-news/', add_news, name='add_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),
    path('news/register/', Register, name='register'),
    path('news/login/', user_login, name='login'),
    path('news/logout/', user_logout, name='logout'),
    path('news/del-news/<int:pk>', Delete_News.as_view(), name='delete'),

    path('news/add-song/', CreateSong.as_view(), name='add_song'),
    path('song/<int:pk>/', ViewSong.as_view(), name='view_song'),
    path('chart/music/', music, name='music'),
    path('chart/', chart, name='chart'),
    path('chart/up/<int:pk>', UpVote, name='up'),
    path('chart/down/<int:pk>', DownVote, name='down'),
]