from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('todolist/', views.todolist, name='todolist'),
    path('create/', views.create, name='create'),
    path('complete/<int:id>/', views.mark_complete, name='mark_complete'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
]