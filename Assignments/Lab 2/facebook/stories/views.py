from django.shortcuts import render
from django.http import HttpResponse


def index(req):
    return HttpResponse('<h2>Welcome to Stories</h2>')
