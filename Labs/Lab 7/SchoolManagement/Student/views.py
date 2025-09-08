from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required # لاستيراد خاصية حماية الصفحات
from .models import Students
from .forms import StudentForm

def home(request):

    return render(request, 'home.html')

def read(request):
    status = request.GET.get('q')
    
    if status in ['True', 'False']:
        student_list = Students.objects.filter(status=(status == 'True'))
    else:
        student_list = Students.objects.all()
        
    student_count = student_list.count()
    
    return render(request, "showstudents.html", {"students": student_list, "student_count": student_count})

def read_one(request, id):

    student = get_object_or_404(Students, id=id)
    return render(request, "student_one.html", {"student": student})

@login_required
def create(request):

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student:show')
    else:
        form = StudentForm()

    return render(request, 'student_form.html', {'form': form, 'page_title': 'إضافة طالب جديد'})

@login_required
def update(request, id):

    student = get_object_or_404(Students, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student:show')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form, 'page_title': 'تعديل بيانات الطالب'})

@login_required
def delete(request, id):

    student = get_object_or_404(Students, id=id)
    if request.method == 'POST': 
        student.delete()
        return redirect("student:show")
    return render(request, 'student_delete_confirm.html', {'student': student})
