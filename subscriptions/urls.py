from django.urls import path
from . import views

urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
    path('success/', views.subscription_success, name='subscribe_success'),  
]