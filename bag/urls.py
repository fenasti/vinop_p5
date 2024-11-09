
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<wine_id>/', views.add_to_bag, name='add_to_bag'),
    path('adjust/<wine_id>/', views.adjust_bag, name='adjust_bag'),
    path('remove/<wine_id>/', views.remove_from_bag, name='remove_from_bag'),
]
