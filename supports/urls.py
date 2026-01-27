from django.urls import path
from . import views

app_name = 'supports'

urlpatterns = [
    path('contact', views.contact, name='contact'),
    path('donation', views.donation, name='donation'),
    path('donation2', views.donation2, name='donation2'),
    path('support', views.support, name='support')    
    
    ]