from django.contrib import admin
from .models import Student
class studentAdmin(admin.ModelAdmin):
    list_display = ['id','name','rollno','subject','dob','phoneno']
admin.site.register(Student,studentAdmin)
