from django.urls import path
from . import views

urlpatterns = [
    path('', views.customers_list, name='customers_list'),
    path('create/', views.create_customer, name='create_customer'),
    path('delete/<int:pk>/', views.delete_customer, name='delete_customer'),
    path('edit/<int:pk>/', views.edit_customer, name='edit_customer'),
]
