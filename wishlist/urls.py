from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist_detail, name='wishlist_detail'),
    path('add/<int:wine_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove/<int:wine_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
]

