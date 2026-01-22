from django.urls import path
from . import views

app_name = 'workshops'

urlpatterns = [
    path('workshop', views.workshop, name='workshop'),
    path('urdu', views.urdu, name='urdu'),
    path('milktea', views.milktea, name='milktea'),
    path('henna', views.henna, name='henna'),
    #path('form', views.form, name='form'),
]