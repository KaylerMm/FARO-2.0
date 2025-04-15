from django.urls import path
from . import views

urlpatterns = [
    path('', views.pet_list, name='pet_list'),
    path('<int:pk>/', views.pet_detail, name='pet_detail'),
    path('create/', views.create_pet, name='create_pet'),
    path('edit/<int:id>/', views.edit_pet, name='edit_pet'),
    path('delete/<int:id>/', views.delete_pet, name='delete_pet'),
    path('delete/confirm/<int:id>/', views.confirm_delete_pet, name='confirm_delete_pet'),
]
