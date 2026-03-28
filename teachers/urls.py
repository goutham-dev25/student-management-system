from django.urls import path

from . import views

app_name = "teachers"

urlpatterns = [
    path("teachers.html", views.teacher_list, name="list"),
    path("teacher-details.html", views.teacher_detail, name="detail"),
    path("add-teacher.html", views.teacher_create, name="add"),
    path("edit-teacher.html", views.teacher_update, name="edit"),
    path("delete-teacher.html", views.teacher_delete, name="delete"),
]
