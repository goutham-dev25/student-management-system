from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TeacherForm
from .models import Teacher


def _get_teacher_from_query(request):
    teacher_id = request.GET.get("teacher")
    if not teacher_id:
        return None
    return get_object_or_404(Teacher, pk=teacher_id)


@login_required
def teacher_list(request):
    return render(request, "teacher/teachers.html", {"teachers": Teacher.objects.all()})


@login_required
def teacher_detail(request):
    teacher = _get_teacher_from_query(request)
    if teacher is None:
        return redirect("teachers:list")
    return render(request, "teacher/teacher-details.html", {"teacher": teacher})


@login_required
def teacher_create(request):
    form = TeacherForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        teacher = form.save()
        messages.success(request, "Teacher added successfully.")
        return redirect(f"{teacher.get_absolute_url()}")
    return render(request, "teacher/add-teacher.html", {"form": form})


@login_required
def teacher_update(request):
    teacher = _get_teacher_from_query(request)
    if teacher is None:
        return redirect("teachers:list")
    form = TeacherForm(request.POST or None, instance=teacher)
    if request.method == "POST" and form.is_valid():
        teacher = form.save()
        messages.success(request, "Teacher updated successfully.")
        return redirect(f"{teacher.get_absolute_url()}")
    return render(request, "teacher/edit-teacher.html", {"form": form, "teacher": teacher})


@login_required
def teacher_delete(request):
    teacher = _get_teacher_from_query(request)
    if teacher is None:
        return redirect("teachers:list")
    if request.method == "POST":
        teacher.delete()
        messages.success(request, "Teacher deleted successfully.")
    return redirect("teachers:list")
