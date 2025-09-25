from django.db import models
from students.models import Student
from django.contrib.auth.models import User
from django.utils import timezone


class Gatepass(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, help_text="Student requesting the gatepass")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time the gatepass was requested")
    date_from = models.DateTimeField(help_text="Start date and time for the gatepass")
    date_to = models.DateTimeField(help_text="End date and time for the gatepass")
    is_suspended = models.BooleanField(default=False, help_text="Indicates if the student's gatepass is suspended")
    date_approved = models.DateTimeField(null=True, blank=True, help_text="Date and time when the gatepass was approved")
    
    @property
    def is_allowed(self):
        return self.date_to > timezone.now() and not self.is_suspended

    def __str__(self):
        return f"Log for {self.student}"

class GateLog(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, help_text="The student being logged")
    entry_time = models.DateTimeField(auto_now=True, help_text="Time when the student entered")

    def __str__(self):
        return f"Log for {self.student}"
