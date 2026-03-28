from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import StudentForm
from .models import Student


def _get_student_from_query(request):
    student_id = request.GET.get("student")
    if not student_id:
        return None
    return get_object_or_404(Student, pk=student_id)


@login_required
def student_list(request):
    return render(request, "student/students.html", {"students": Student.objects.all()})


@login_required
def student_detail(request):
    student = _get_student_from_query(request)
    if student is None:
        return redirect("students:list")
    return render(request, "student/student-details.html", {"student": student})


@login_required
def student_create(request):
    form = StudentForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        student = form.save()
        messages.success(request, "Student added successfully.")
        return redirect(f"{student.get_absolute_url()}")
    return render(request, "student/add-student.html", {"form": form})


@login_required
def student_update(request):
    student = _get_student_from_query(request)
    if student is None:
        return redirect("students:list")
    form = StudentForm(request.POST or None, request.FILES or None, instance=student)
    if request.method == "POST" and form.is_valid():
        student = form.save()
        messages.success(request, "Student updated successfully.")
        return redirect(f"{student.get_absolute_url()}")
    return render(request, "student/edit-student.html", {"form": form, "student": student})


@login_required
def student_delete(request):
    student = _get_student_from_query(request)
    if student is None:
        return redirect("students:list")
    if request.method == "POST":
        student.delete()
        messages.success(request, "Student deleted successfully.")
    return redirect("students:list")
