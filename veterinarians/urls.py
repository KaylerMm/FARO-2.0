from django.urls import path
from . import views

urlpatterns = [
    path('', views.veterinarian_list, name='veterinarian_list'),
    path('create/', views.create_veterinarian, name='create_veterinarian'),
    path('<int:pk>/edit/', views.update_veterinarian, name='update_veterinarian'),
    path('<int:pk>/delete/', views.delete_veterinarian, name='delete_veterinarian'),
    path('<int:pk>/', views.veterinarian_detail, name='veterinarian_detail'),
]
