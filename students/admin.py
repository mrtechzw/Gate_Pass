from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display =('id','full_name', 'grade', 'classroom', 'guardian_name')
    search_fields = ('full_name', 'guardian_name')
    list_filter = ('grade', 'classroom', 'gender')