from django.contrib import admin

from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "full_name", "student_class", "section", "mobile_number")
    search_fields = ("student_id", "admission_number", "first_name", "last_name", "father_name")
    list_filter = ("gender", "student_class", "section")
