from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .forms import EmailComposerForm
from datetime import datetime 

def email_composer_view(request):
    message = None
    success = False

    if request.method == 'POST':
        form = EmailComposerForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            
            instructor_email = cleaned_data.get('instructor_email')
            student_name = cleaned_data.get('student_name')
            email_title = cleaned_data.get('email_title')
            email_body = cleaned_data.get('email_body')
            closing_remarks = cleaned_data.get('closing_remarks')

            current_time = datetime.now().strftime("%Y-%m-%d, %I:%M %p")

            context = {
                'title': email_title,
                'body': email_body,
                'closing_remarks': closing_remarks,
                'student_name': student_name,
                'sent_at': current_time, 
            }
            html_message = render_to_string('emails/project_summary_email.html', context)
            
            try:
                send_mail(
                    subject=f"ملخص مشروع: {email_title} - {student_name}",
                    message='This is an HTML email.',
                    from_email=None,
                    recipient_list=[instructor_email],
                    html_message=html_message,
                    fail_silently=False,
                )
                message = f"تم إرسال البريد بنجاح إلى {instructor_email}!"
                success = True
                form = EmailComposerForm()
            except Exception as e:
                message = f"حدث خطأ: {e}"
                success = False

    else:
        form = EmailComposerForm()

    return render(request, 'emails/compose_email.html', {'form': form, 'message': message, 'success': success})

