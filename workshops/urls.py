from django.urls import path
from . import views

app_name = 'workshops'

urlpatterns = [
    path('workshop', views.workshop, name='workshop'),
    path('form', views.form, name='form'),
    path('tutor1', views.tutor1, name='tutor1'),
    path('tutor2', views.tutor2, name='tutor2'),
]