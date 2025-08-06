from django.shortcuts import render
from .data import context
# Create your views here.
def index(request):
    return render(request, 'webPage.html', {'students':context})


def home(request):
    return render(request, 'home.html')

def list_students(request):
    students = {
        'name':'dheya',
        'marks':[91, 80, 86],
        'each':{
            'theory':65,
            'programming':80
        },
        'total':300
    }
    return render(request, 'showstudents.html', students)

def edit_students(request):
    return render(request, 'editstudents.html')

def deletestudents(request):
    return render(request, 'deletestudents.html')