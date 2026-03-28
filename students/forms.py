from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            "first_name",
            "last_name",
            "student_id",
            "gender",
            "date_of_birth",
            "student_class",
            "religion",
            "joining_date",
            "mobile_number",
            "admission_number",
            "section",
            "student_image",
            "father_name",
            "father_occupation",
            "father_mobile",
            "father_email",
            "mother_name",
            "mother_occupation",
            "mother_mobile",
            "mother_email",
            "present_address",
            "permanent_address",
        ]
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
            "joining_date": forms.DateInput(attrs={"type": "date"}),
        }
