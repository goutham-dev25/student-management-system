from django import forms

from .models import Teacher


class TeacherForm(forms.ModelForm):
    password = forms.CharField(required=False, widget=forms.PasswordInput(render_value=True))
    repeat_password = forms.CharField(required=False, widget=forms.PasswordInput(render_value=True))

    class Meta:
        model = Teacher
        fields = [
            "teacher_id",
            "name",
            "gender",
            "date_of_birth",
            "mobile",
            "joining_date",
            "qualification",
            "experience",
            "username",
            "email",
            "address",
            "city",
            "state",
            "zip_code",
            "country",
        ]
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
            "joining_date": forms.DateInput(attrs={"type": "date"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        repeat_password = cleaned_data.get("repeat_password")
        if password or repeat_password:
            if password != repeat_password:
                self.add_error("repeat_password", "Passwords do not match.")
        return cleaned_data
