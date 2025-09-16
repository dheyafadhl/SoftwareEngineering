# نفترض أن اسم النموذج هو 'Student' (بالمفرد) وفقًا لأساسيات Django
from .models import Students
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from notifications.signals import notify


@receiver(post_save, sender=Students)
def student_created_or_update_notification(sender, instance, created, **kwargs):
    """
    ترسل هذه الدالة إشعارات للمسؤولين عند إضافة طالب أو تحديثه.
    """
    admins = User.objects.filter(is_staff=True)
    
    if created:
        # هذا الجزء يعمل فقط عند إنشاء طالب جديد
        verb = "تم إضافة طالب جديد"
        description = f"تم إضافة الطالب {instance.f_name} {instance.l_name}"
    else:
        # هذا الجزء يعمل فقط عند تحديث طالب موجود
        # تم إزالة شرط 'if instance.state.adding' الذي كان يسبب المشكلة
        verb = "تم تعديل بيانات طالب"
        description = f"تم تعديل بيانات الطالب {instance.f_name} {instance.l_name}"

    for admin in admins:
        notify.send(instance, recipient=admin, verb=verb, description=description)


@receiver(post_delete, sender=Students)
def student_delete_notification(sender, instance, **kwargs): # تم إصلاح الخطأ الإملائي في اسم الدالة
    """
    ترسل هذه الدالة إشعارات للمسؤولين عند حذف طالب.
    """
    admins = User.objects.filter(is_staff=True)
    for admin in admins:
        notify.send(
            instance,
            recipient=admin,
            verb='تم حذف طالب',
            description=f'تم حذف الطالب {instance.f_name} {instance.l_name} من النظام'
        )