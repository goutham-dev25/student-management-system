from django.contrib.auth.decorators import login_required
from django.shortcuts import render


STATIC_TEMPLATE_MAP = {
    "index.html": "index.html",
    "teacher-dashboard.html": "teacher/teacher-dashboard.html",
    "student-dashboard.html": "student/student-dashboard.html",
    "departments.html": "department/departments.html",
    "add-department.html": "department/add-department.html",
    "edit-department.html": "department/edit-department.html",
    "subjects.html": "subject/subjects.html",
    "add-subject.html": "subject/add-subject.html",
    "edit-subject.html": "subject/edit-subject.html",
    "fees-collections.html": "account/fees-collections.html",
    "expenses.html": "account/expenses.html",
    "salary.html": "account/salary.html",
    "add-fees-collection.html": "account/add-fees-collection.html",
    "add-expenses.html": "account/add-expenses.html",
    "add-salary.html": "account/add-salary.html",
    "add-fees.html": "account/add-fees.html",
    "edit-fees.html": "account/edit-fees.html",
    "fees.html": "home/fees.html",
    "exam.html": "home/exam.html",
    "event.html": "home/event.html",
    "time-table.html": "home/time-table.html",
    "library.html": "home/library.html",
    "inbox.html": "home/inbox.html",
    "sports.html": "others/sports.html",
    "hostel.html": "others/hostel.html",
    "transport.html": "others/transport.html",
    "blank-page.html": "pages/blank-page.html",
    "forgot-password.html": "pages/forgot-password.html",
    "error-404.html": "pages/error-404.html",
    "components.html": "components.html",
    "form-basic-inputs.html": "form-basic-inputs.html",
    "form-input-groups.html": "form-input-groups.html",
    "form-horizontal.html": "form-horizontal.html",
    "form-vertical.html": "form-vertical.html",
    "form-mask.html": "form-mask.html",
    "form-validation.html": "form-validation.html",
    "tables-basic.html": "tables-basic.html",
}


@login_required
def static_page(request, page_name):
    return render(request, STATIC_TEMPLATE_MAP[page_name])
