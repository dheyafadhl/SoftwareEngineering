from django.urls import path
from . import views

app_name = 'department'

urlpatterns = [
    path('', views.department_list, name='list'),
    path('create/', views.department_create, name='create'),
    path('update/<int:id>/', views.department_update, name='update'),
    path('delete/<int:id>/', views.department_delete, name='delete'),
]
