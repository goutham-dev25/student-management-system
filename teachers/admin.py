from django.contrib import admin

from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("teacher_id", "name", "qualification", "mobile", "email")
    search_fields = ("teacher_id", "name", "username", "email")
    list_filter = ("gender", "qualification")
