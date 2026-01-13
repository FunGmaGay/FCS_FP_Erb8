from django.urls import path #from module import function
from . import views #from current folder import file

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about')
]