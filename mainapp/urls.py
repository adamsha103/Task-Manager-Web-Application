from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_redirect, name='home'),  
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('add/', views.add_task, name='add_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('logout/', views.logout_view, name='logout'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('', views.task_list, name='task_list'),  

]
