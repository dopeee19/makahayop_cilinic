from django.urls import path
from . import views


urlpatterns = [

    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('', views.home, name='home'),
    path('dashboard/', views.dashboard_view, name='dashboard'),

    path('appointment/', views.appointment_list, name='appointment_list'),
    path('appointment/<int:pk>/', views.appointment_detail, name='appointment_detail'),
    path('appointment/create/', views.appointment_create, name='appointment_create'),
     path('customerappointment/create/', views.customerappointment_create, name='customerappointment_create'),
    path('appointment/<int:pk>/update/', views.appointment_update, name='appointment_update'),
    path('appointment/<int:pk>/delete/', views.appointment_delete, name='appointment_delete'),


    path('services/', views.service_list, name='service_list'),
    path('services/<int:pk>/', views.service_detail, name='service_detail'),
    path('services/create/', views.service_create, name='service_create'),
    path('services/<int:pk>/update/', views.service_update, name='service_update'),
    path('services/<int:pk>/delete/', views.service_delete, name='service_delete'),

     path('vets/', views.vet_list, name='vet_list'),
    path('vets/<int:pk>/', views.vet_detail, name='vet_detail'),
    path('vets/create/', views.vet_create, name='vet_create'),
    path('vets/<int:pk>/update/', views.vet_update, name='vet_update'),
    path('vets/<int:pk>/delete/', views.vet_delete, name='vet_delete'),


     path('feedback/', views.feedback_list, name='feedback_list'),
    path('feedback/create/', views.feedback_create, name='feedback_create'),

]
