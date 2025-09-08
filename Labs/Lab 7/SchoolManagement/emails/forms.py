from django import forms

class EmailComposerForm(forms.Form):
    instructor_email = forms.EmailField(
        label="إيميل المدرس",
        widget=forms.EmailInput(attrs={'class': 'w-full bg-gray-600 text-white p-2 rounded border border-gray-500 focus:ring-2 focus:ring-[#25A6B7] focus:border-[#25A6B7] outline-none', 'placeholder': 'ادخل إيميل المدرس هنا'})
    )
    student_name = forms.CharField(
        label="اسمك",
        widget=forms.TextInput(attrs={'class': 'w-full bg-gray-600 text-white p-2 rounded border border-gray-500 focus:ring-2 focus:ring-[#25A6B7] focus:border-[#25A6B7] outline-none', 'placeholder': 'اسمك الكامل'})
    )
    email_title = forms.CharField(
        label="عنوان الرسالة (سيظهر كـ H1 في الإيميل)",
        widget=forms.TextInput(attrs={'class': 'w-full bg-gray-600 text-white p-2 rounded border border-gray-500 focus:ring-2 focus:ring-[#25A6B7] focus:border-[#25A6B7] outline-none', 'placeholder': 'مثال: ملخص مشروع مقارنة ثيمات Django'})
    )
    email_body = forms.CharField(
        label="محتوى الرسالة الأساسي",
        widget=forms.Textarea(attrs={'class': 'w-full bg-gray-600 text-white p-2 rounded border border-gray-500 focus:ring-2 focus:ring-[#25A6B7] focus:border-[#25A6B7] outline-none', 'rows': 6, 'placeholder': 'اكتب هنا شرحًا للمشروع، الميزات الرئيسية، والتقنيات المستخدمة...'})
    )
    closing_remarks = forms.CharField(
        label="انطباعات ختامية (اختياري)",
        required=False,
        widget=forms.Textarea(attrs={'class': 'w-full bg-gray-600 text-white p-2 rounded border border-gray-500 focus:ring-2 focus:ring-[#25A6B7] focus:border-[#25A6B7] outline-none', 'rows': 3, 'placeholder': 'مثل: انطباعك عن المقرر، التدريس، إلخ.'})
    )
