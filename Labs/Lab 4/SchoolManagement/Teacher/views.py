from django.shortcuts import render
from .data import context
# Create your views here.

def teacher(request):
    return render (request, 'showteachers.html', {'teachers': context})