from django.db import models
from django.urls import reverse


class Student(models.Model):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Others", "Others"),
    ]

    student_id = models.CharField(max_length=30, unique=True)
    admission_number = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    student_class = models.CharField(max_length=20)
    section = models.CharField(max_length=10)
    religion = models.CharField(max_length=50, blank=True)
    joining_date = models.DateField()
    mobile_number = models.CharField(max_length=20)
    student_image = models.FileField(upload_to="students/", blank=True, null=True)
    father_name = models.CharField(max_length=150)
    father_occupation = models.CharField(max_length=100, blank=True)
    father_mobile = models.CharField(max_length=20, blank=True)
    father_email = models.EmailField(blank=True)
    mother_name = models.CharField(max_length=150, blank=True)
    mother_occupation = models.CharField(max_length=100, blank=True)
    mother_mobile = models.CharField(max_length=20, blank=True)
    mother_email = models.EmailField(blank=True)
    present_address = models.TextField()
    permanent_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["student_id"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}".strip()

    @property
    def full_name(self):
        return str(self)

    @property
    def parent_name(self):
        return self.father_name or self.mother_name

    def get_absolute_url(self):
        return f"{reverse('students:detail')}?student={self.pk}"
