from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('', views.home, name="home"),
    
    path('student/', views.student, name="student"),
    path('test/', views.test_page, name="test"),

    path('show/', views.list_students, name="show"),
    path('edit/', views.edit_students, name="edit"),
    path('delete/', views.edit_students, name="delete"),
]