from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Teacher
from .forms import TeacherForm

@login_required
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teachers': teachers})

@login_required
def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Teacher:list')
    else:
        form = TeacherForm()
    return render(request, 'teacher_form.html', {'form': form})

@login_required
def teacher_update(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('Teacher:list')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'teacher_form.html', {'form': form, 'teacher': teacher})

@login_required
def teacher_delete(request, id):
    try:
        teacher = Teacher.objects.get(id=id)
        if request.method == 'POST':
            teacher.delete()
            messages.success(request, f"تم حذف المدرس '{teacher}' بنجاح.")
            return redirect('Teacher:list')
        
        return render(request, 'teacher_confirm_delete.html', {'object': teacher})

    except Teacher.DoesNotExist:
        messages.error(request, "المدرس الذي تحاول حذفه غير موجود.")
        return redirect('Teacher:list')
