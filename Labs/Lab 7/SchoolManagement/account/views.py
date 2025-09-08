from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def signup(request):
    if request.user.is_authenticated:
        return redirect('student:home')
        
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'تم إنشاء حسابك بنجاح، مرحباً بك يا {user.username}!')
            return redirect('student:show')
        else:
            messages.error(request, 'حدث خطأ ما، يرجى مراجعة البيانات المدخلة.')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

