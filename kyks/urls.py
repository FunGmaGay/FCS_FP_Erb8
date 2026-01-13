from django.urls import path
from . import views

app_name = 'kyks'

urlpatterns = [
    path('activity', views.activity, name='activity'),
    path('album1', views.album1, name='album1'),
    path('album2', views.album2, name='album2'),   
    path('kyk', views.kyk, name='kyk'),
    path('media', views.media, name='media'),
    path('news', views.news, name='news'),
    ]