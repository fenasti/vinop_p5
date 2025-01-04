from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:wine_id>/', views.add_review, name='add_review'),
]