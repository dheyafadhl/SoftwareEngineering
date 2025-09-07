from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم القسم")
    head = models.CharField(max_length=100, verbose_name="رئيس القسم")

    def __str__(self):
        return self.name
