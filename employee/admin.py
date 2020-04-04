from django.contrib import admin
from employee.models import Employee


# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno','ename_name']

admin.site.register(Employee)
