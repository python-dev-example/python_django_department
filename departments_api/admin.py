from django.contrib import admin

from departments_api.models import Department, Employee


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'email', 'birthday', 'salary')


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
