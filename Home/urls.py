"""
URL configuration for Home project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .views import static_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("authentication.urls")),
    path("", include("students.urls")),
    path("", include("teachers.urls")),
    path("", static_page, {"page_name": "index.html"}, name="home"),
    path("index.html", static_page, {"page_name": "index.html"}, name="dashboard"),
    path("teacher-dashboard.html", static_page, {"page_name": "teacher-dashboard.html"}, name="teacher-dashboard"),
    path("student-dashboard.html", static_page, {"page_name": "student-dashboard.html"}, name="student-dashboard"),
    path("departments.html", static_page, {"page_name": "departments.html"}, name="departments"),
    path("add-department.html", static_page, {"page_name": "add-department.html"}, name="add-department"),
    path("edit-department.html", static_page, {"page_name": "edit-department.html"}, name="edit-department"),
    path("subjects.html", static_page, {"page_name": "subjects.html"}, name="subjects"),
    path("add-subject.html", static_page, {"page_name": "add-subject.html"}, name="add-subject"),
    path("edit-subject.html", static_page, {"page_name": "edit-subject.html"}, name="edit-subject"),
    path("fees-collections.html", static_page, {"page_name": "fees-collections.html"}, name="fees-collections"),
    path("expenses.html", static_page, {"page_name": "expenses.html"}, name="expenses"),
    path("salary.html", static_page, {"page_name": "salary.html"}, name="salary"),
    path("add-fees-collection.html", static_page, {"page_name": "add-fees-collection.html"}, name="add-fees-collection"),
    path("add-expenses.html", static_page, {"page_name": "add-expenses.html"}, name="add-expenses"),
    path("add-salary.html", static_page, {"page_name": "add-salary.html"}, name="add-salary"),
    path("add-fees.html", static_page, {"page_name": "add-fees.html"}, name="add-fees"),
    path("edit-fees.html", static_page, {"page_name": "edit-fees.html"}, name="edit-fees"),
    path("fees.html", static_page, {"page_name": "fees.html"}, name="fees"),
    path("exam.html", static_page, {"page_name": "exam.html"}, name="exam"),
    path("event.html", static_page, {"page_name": "event.html"}, name="event"),
    path("time-table.html", static_page, {"page_name": "time-table.html"}, name="time-table"),
    path("library.html", static_page, {"page_name": "library.html"}, name="library"),
    path("inbox.html", static_page, {"page_name": "inbox.html"}, name="inbox"),
    path("sports.html", static_page, {"page_name": "sports.html"}, name="sports"),
    path("hostel.html", static_page, {"page_name": "hostel.html"}, name="hostel"),
    path("transport.html", static_page, {"page_name": "transport.html"}, name="transport"),
    path("blank-page.html", static_page, {"page_name": "blank-page.html"}, name="blank-page"),
    path("forgot-password.html", static_page, {"page_name": "forgot-password.html"}, name="forgot-password"),
    path("error-404.html", static_page, {"page_name": "error-404.html"}, name="error-404"),
    path("components.html", static_page, {"page_name": "components.html"}, name="components"),
    path("form-basic-inputs.html", static_page, {"page_name": "form-basic-inputs.html"}, name="form-basic-inputs"),
    path("form-input-groups.html", static_page, {"page_name": "form-input-groups.html"}, name="form-input-groups"),
    path("form-horizontal.html", static_page, {"page_name": "form-horizontal.html"}, name="form-horizontal"),
    path("form-vertical.html", static_page, {"page_name": "form-vertical.html"}, name="form-vertical"),
    path("form-mask.html", static_page, {"page_name": "form-mask.html"}, name="form-mask"),
    path("form-validation.html", static_page, {"page_name": "form-validation.html"}, name="form-validation"),
    path("tables-basic.html", static_page, {"page_name": "tables-basic.html"}, name="tables-basic"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
