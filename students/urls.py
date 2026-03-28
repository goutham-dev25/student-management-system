from django.urls import path

from . import views

app_name = "students"

urlpatterns = [
    path("students.html", views.student_list, name="list"),
    path("student-details.html", views.student_detail, name="detail"),
    path("add-student.html", views.student_create, name="add"),
    path("edit-student.html", views.student_update, name="edit"),
    path("delete-student.html", views.student_delete, name="delete"),
]
