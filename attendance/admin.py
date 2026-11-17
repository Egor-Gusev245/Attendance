from django.contrib import admin
from .models import Users, Attendance

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')
    search_fields = ('name',)

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'datetime', 'student', 'marked')
    list_filter = ('marked', 'datetime', 'lesson')
    search_fields = ('lesson', 'student__name', 'marked')

