from django.urls import path
from . import views

app_name = 'enrolments'

urlpatterns = [
    path('apply/<int:workshop_id>/', views.apply, name='apply'),
]