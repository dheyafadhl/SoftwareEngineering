from django.urls import path
from . import views

app_name = 'student'
urlpatterns = [
    path('', views.home, name='home'),
    path('all/', views.read, name='show'),
    path('one/<int:id>/', views.read_one, name='student_one'),
    path('create/', views.create, name='newstudent'),
    path('update/<int:id>/', views.update, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
]