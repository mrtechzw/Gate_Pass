from django.contrib import admin
from django.http import JsonResponse
from django.db import transaction
from django.utils import timezone
from .models import Gatepass, GateLog, Student
import json


admin.site.site_header=" Access Point Gate Pass System"
admin.site.site_title="Access Point"
admin.site.index_title="Access Point Mini Admin"

@admin.register(Gatepass)
class GatepassAdmin(admin.ModelAdmin):
    list_display = ('student', 'is_suspended', 'created_at', 'date_from', 'date_to',)
    list_filter = ('is_suspended', 'created_at',)
    search_fields = ('student__full_name',)
    autocomplete_fields = ['student',]
    readonly_fields = []

@admin.register(GateLog)
class GateLogAdmin(admin.ModelAdmin):
    list_display = ('student', 'entry_time')
    search_fields = ('student__full_name',)
    def add_view(self, request, form_url='', extra_context=None):
        
        if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
            try:
                with transaction.atomic():
                    # Assuming we get these values from the POST request (modify as needed)
                    student_id = request.POST.get('student_id')  # Student ID to identify the student  
                    # Fetch the student object
                    student = Student.objects.get(id=student_id)

                if Gatepass.objects.filter(student=student, date_to__gt=timezone.now(), is_suspended=False).exists():
                    if GateLog.objects.filter(student=student, entry_time__date=timezone.now().date()).exists():
                         return JsonResponse({'success': False, 'error_message': 'GatePass used today'})
                    else:
                        GateLog.objects.create(student=student)
                    return JsonResponse({'success': True, 'message': 'Student is allowed'})
                else:
                    return JsonResponse({'success': False, 'error_message': 'Student is not allowed'})    

            except Exception as e:
                return JsonResponse({'success': False, 'error_message': 'Studnet not found'}, status=400)

        extra_context = extra_context or {}
        students = Student.objects.all()
        extra_context['title'] = 'Scan Student ID'
        extra_context['students_json'] = json.dumps([
    {
        'id': student.id,
        'full_name': student.full_name,
        'gender': student.gender,
        'date_of_birth': student.date_of_birth.strftime('%d-%m-%Y'),
        'image': student.image.url
    } for student in students
])

        self.change_form_template = "admin/scan_add.html"
        return super().add_view(request, form_url, extra_context=extra_context)

    def change_view(self, request, object_id, *args, **kwargs):
        self.change_form_template = "admin/change_form.html"
        return super().change_view(request, object_id, *args, **kwargs)

