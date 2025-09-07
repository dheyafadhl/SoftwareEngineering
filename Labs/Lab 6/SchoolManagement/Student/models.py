from django.db import models
from django.contrib.auth.models import User
# from django.db import models
from department.models import Department
from Teacher.models import Teacher       

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True, verbose_name="نبذة تعريفية")
    

    def __str__(self):
        return self.user.username

class Students(models.Model):
    Levels = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')]
    f_name = models.CharField(max_length=10, verbose_name="الاسم الأول")
    l_name = models.CharField(max_length=10, verbose_name="الاسم الأخير")
    age = models.IntegerField(verbose_name="العمر")
    level = models.CharField(choices=Levels, max_length=20, verbose_name="المستوى")
    gpa = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="المعدل")
    status = models.BooleanField(verbose_name="الحالة (فعال)")
    report = models.TextField(max_length=300, verbose_name="التقرير")
    image = models.ImageField(upload_to='images/%y/%m/%d', null=True, blank=True, verbose_name="الصورة")
    file_report = models.FileField(upload_to='files/%y/%m/%d', null=True, blank=True, verbose_name="ملف التقرير")

    
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="القسم")
    
    teachers = models.ManyToManyField(Teacher, blank=True, verbose_name="المدرسون")

    def __str__(self):
        return f"{self.f_name} {self.l_name}"
    
    def delete(self):
        self.image.delete()
        self.file_report.delete()
        return super().delete()
