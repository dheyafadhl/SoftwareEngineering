from django.db import models
from department.models import Department

class Teacher(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="الاسم الأول")
    last_name = models.CharField(max_length=50, verbose_name="الاسم الأخير")
    age = models.IntegerField(verbose_name="العمر")
    GENDER_CHOICES = [
        ('ذكر', 'ذكر'),
        ('أنثى', 'أنثى'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name="الجنس")
    specialization = models.CharField(max_length=100, verbose_name="التخصص")
    is_head_of_department = models.BooleanField(default=False, verbose_name="هل هو رئيس قسم؟")

    email = models.EmailField(unique=True, null=True, blank=True, verbose_name="البريد الإلكتروني")
    phone_number = models.CharField(max_length=20, null=True, blank=True, verbose_name="رقم الهاتف")
    image = models.ImageField(upload_to='teachers_images/%y/%m/%d', null=True, blank=True, verbose_name="الصورة الشخصية")
    cv_file = models.FileField(upload_to='teachers_files/%y/%m/%d', null=True, blank=True, verbose_name="ملف السيرة الذاتية")

    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="القسم", null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "مدرس"
        verbose_name_plural = "المدرسين"

