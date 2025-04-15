from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('', views.appointment_list, name='appointment_list'),
    path('<int:pk>/', views.appointment_detail, name='appointment_detail'),
    path('create/', views.appointment_create, name='appointment_create'),
    path('<int:pk>/edit/', views.appointment_update, name='appointment_update'),
    path('<int:pk>/delete/', views.appointment_delete, name='appointment_delete'),
]
