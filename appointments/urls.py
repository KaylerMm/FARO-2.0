from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('', views.appointment_list, name='appointment_list'),
    path('<int:pk>/', views.appointment_detail, name='appointment_detail'),
    path('create/', views.appointment_create, name='appointment_create'),
    path('<int:pk>/edit/', views.appointment_update, name='appointment_update'),
    path('<int:pk>/delete/', views.appointment_delete, name='appointment_delete'),
    path('<int:appointment_id>/medical-record/', views.view_medical_record, name='view_medical_record'),
    path('<int:appointment_id>/medical-record/create/', views.create_medical_record, name='create_medical_record'),
    path('<int:appointment_id>/medical_record_edit/', views.edit_medical_record, name='edit_medical_record'),
    path('appointments/<int:appointment_id>/medical_record_delete/', views.delete_medical_record, name='delete_medical_record'),
]
