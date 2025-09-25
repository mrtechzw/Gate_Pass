from django.db import models


class Student(models.Model):
    full_name = models.CharField(max_length=100, help_text="Full name of the student")
    date_of_birth = models.DateField(help_text="Date of birth of the student")
    gender = models.CharField(
        max_length=10,
        choices=[('Male', 'Male'), ('Female', 'Female')],
        help_text="Gender of the student"
    )
    address = models.TextField(help_text="Home address of the student")
    guardian_name = models.CharField(max_length=100, help_text="Name of the student's guardian")
    guardian_contact = models.CharField(max_length=20, help_text="Contact number of the guardian")
    grade = models.CharField(max_length=10, help_text="Grade the student is currently enrolled in")
    classroom = models.CharField(max_length=10, help_text="Classroom or section of the student")
    image = models.ImageField(upload_to='student_images/', null=True, blank=True, help_text="Photograph of the student")

    @property
    def image_url(self):
        return self.image.url

    def __str__(self):
        return f"{self.full_name}"