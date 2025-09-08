from django.urls import path
from . import views

app_name = 'Teacher'

urlpatterns = [
    # path('', views.teacher_list, name='list'),
    path('list/', views.teacher_list, name='list'),
    path('create/', views.teacher_create, name='create'),
    path('<int:id>/update/', views.teacher_update, name='update'),
    path('<int:id>/delete/', views.teacher_delete, name='delete'),
]

