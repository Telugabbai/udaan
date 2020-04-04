from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    salary = models.IntegerField()
    city = models.CharField(max_length=20)
    dept = models.CharField(max_length=20)

    def __str__(self):
        return self.emp_name
