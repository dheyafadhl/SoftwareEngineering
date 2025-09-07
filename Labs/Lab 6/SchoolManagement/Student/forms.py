from django import forms
from .models import Students

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        # تحديد الحقول بشكل صريح أفضل من '__all__'
        fields = ['f_name', 'l_name', 'age', 'level', 'gpa', 'status', 'report', 'image', 'file_report']
        
        # إضافة تسميات عربية للحقول
        labels = {
            'f_name': 'الاسم الأول',
            'l_name': 'الاسم الأخير',
            'age': 'العمر',
            'level': 'المستوى الدراسي',
            'gpa': 'المعدل التراكمي',
            'status': 'الحالة (فعال)',
            'report': 'التقرير الكتابي',
            'image': 'صورة الطالب',
            'file_report': 'ملف التقرير',
        }
        
        # يمكننا إضافة عناصر تحكم إضافية هنا إذا أردنا
        widgets = {
            'report': forms.Textarea(attrs={'rows': 4}),
        }
