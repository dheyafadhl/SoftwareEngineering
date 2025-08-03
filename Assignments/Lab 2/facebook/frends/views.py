from django.shortcuts import render
from django.http import HttpResponse


def index(req):
    return HttpResponse('<h2>Sorry, but you don\'t have any frends, you so lonely :`(</h2>')