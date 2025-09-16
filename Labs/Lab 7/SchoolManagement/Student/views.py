from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required # لاستيراد خاصية حماية الصفحات
from .models import Students
from .forms import StudentForm
from notifications.models import Notification

def home(request):
    # جلب الإشعارات الخاصة بالمستخدم الحالي فقط
    user_notifications = Notification.objects.filter(recipient=request.user)

    # حساب عدد الإشعارات غير المقروءة
    unread_count = user_notifications.filter(unread=True).count()
    
    # حساب العدد الإجمالي للإشعارات
    total_count = user_notifications.count()

    context = {
        "notificationCount": unread_count, 
        
        "all_notification_count": total_count,
        
        "notification" : user_notifications 
    }
    return render(request, 'home.html', context)

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



@login_required(login_url='account:login')
def readnotification(request, pk):
    try:
        notifications = Notification.objects.get(id=pk)
        notifications.unread = False
        notifications.save()
    except Notification.DoesNotExist:
        return redirect('notifications:error_page')
    return redirect('student:show')

def deletenotification(request, pk):
    notification = Notification.objects.get(id=pk).delete()
    return redirect('student:home')