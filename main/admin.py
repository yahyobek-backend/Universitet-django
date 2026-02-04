from django.contrib import admin

from main.models import Subject, Direction, Teacher

# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name','age', 'level', 'gender', 'subject')
    search_fields = ('name',)

class DirectionAdmin(admin.ModelAdmin):
    list_display = ('name','is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name','is_main', 'direction')
    list_filter = ('is_main', 'direction')
    search_fields = ('name',)

admin.site.register(Direction, DirectionAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Teacher, TeacherAdmin)
