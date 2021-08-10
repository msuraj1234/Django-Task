from django.contrib import admin
from .models import StudentModel


# Register your models here.
@admin.register(StudentModel)
class stuAdmin(admin.ModelAdmin):
    list_display = ['name']