from django.urls import path
from . import views

app_name = 'enrolments'

urlpatterns = [
    path('apply', views.apply, name='apply'),
]