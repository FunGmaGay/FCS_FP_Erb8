from django.urls import path
from . import views

app_name = 'enrolments'

urlpatterns = [
    path('enrolment', views.enrolment, name='enrolment'),
]