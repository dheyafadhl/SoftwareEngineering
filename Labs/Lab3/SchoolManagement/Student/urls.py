from django.urls import path
from . import views


urlpatterns = [
    path('', views.test_page, name="test"),
    path('index/', views.index, name="index"),

    path('home/', views.home, name="home"),
    path('show/', views.list_students, name="show"),
    # path('edit/', views.edit_students, name="edit"),
    # path('delete/', views.edit_students, name="delete"),
]