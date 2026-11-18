from django.utils import timezone
from django.shortcuts import render, redirect
from .models import Users, Attendance

def view_student(request):
    selected_group = request.GET.get('group')
    if selected_group:
        students = Users.objects.filter(group=selected_group).order_by('name')
    else:
        students = Users.objects.none()
    context = {'students': students, 'selected_group': selected_group}
    return render(request, 'attendance/attendance_list.html', context)

def view_attendance(request):
    if request.method == 'POST':
        lesson = request.POST.get('lesson')
        present_ids = request.POST.getlist('present_students')
        selected_group = request.POST.get('group')
        students = Users.objects.filter(group=selected_group).order_by('name')
        for student in students:
            if str(student.id) in present_ids:
                status = 1
            else:
                status = 0
            Attendance.objects.create(lesson=lesson, student_id=student.id, datetime=timezone.now(), marked=status)
        return redirect(f'/attendance/?group={selected_group}')