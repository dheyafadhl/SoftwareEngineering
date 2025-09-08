from django.urls import path
from . import views

urlpatterns = [
    path('compose/', views.email_composer_view, name='compose_email'),
]
