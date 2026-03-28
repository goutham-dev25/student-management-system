from django.db import models
from django.urls import reverse


class Teacher(models.Model):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Others", "Others"),
    ]

    teacher_id = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=150)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    mobile = models.CharField(max_length=20)
    joining_date = models.DateField()
    qualification = models.CharField(max_length=150)
    experience = models.PositiveIntegerField(help_text="Experience in years")
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["teacher_id"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"{reverse('teachers:detail')}?teacher={self.pk}"
