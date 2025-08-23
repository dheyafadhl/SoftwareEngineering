from django import template
import math

register = template.Library()

@register.filter(name='reading_time')
def reading_time(value, words_per_minute=200):
    """
    يحسب وقت قراءة تقديري لكتلة من النص.
    'value' هو محتوى النص الذي يتم تمريره إلى الفلتر.
    'words_per_minute' هي وسيطة اختيارية، قيمتها الافتراضية 200.

    الاستخدام في القالب:
    {{ my_text_variable|reading_time }}
    أو
    {{ my_text_variable|reading_time:250 }}
    """

    # التأكد من أن المدخل هو سلسلة نصية لتجنب الأخطاء
    if not isinstance(value, str):
        return ""

    # حساب عدد الكلمات في النص
    word_count = len(value.split())

    # حساب عدد الدقائق، مع التقريب لأعلى إلى أقرب عدد صحيح
    minutes = math.ceil(word_count / int(words_per_minute))

    if minutes < 1:
        return "أقل من دقيقة قراءة"
    elif minutes == 1:
        return "دقيقة واحدة قراءة"
    else:
        return f"{minutes} دقائق قراءة"