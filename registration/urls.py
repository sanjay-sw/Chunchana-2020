from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('registration_success/', views.registration_success, name='success'),
    path('branch_administration/', views.view_participants, name='branch_admin'),
    path('delete_info/<str:pk>', views.delete, name='delete'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
]
