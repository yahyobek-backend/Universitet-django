from django.contrib import admin

from main.models import Subject, Direction, Teacher

# Register your models here.

admin.site.register(Direction)
admin.site.register(Subject)
admin.site.register(Teacher)
