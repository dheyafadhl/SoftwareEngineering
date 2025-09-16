from django.urls import path
from . import views

app_name = 'student'
urlpatterns = [
    path('', views.home, name='home'),
    path('read/<int:pk>/', views.readnotification, name='read'),
    path('del/<int:pk>/', views.deletenotification, name='dele'),
    path('all/', views.read, name='show'),
    path('one/<int:id>/', views.read_one, name='student_one'),
    path('create/', views.create, name='newstudent'),
    path('update/<int:id>/', views.update, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
