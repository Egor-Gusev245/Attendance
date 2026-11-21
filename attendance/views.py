from django.utils import timezone
from django.shortcuts import render, redirect
from .models import Users, Attendance

def view_student(request):
    selected_group = request.GET.get('group')
    selected_date = request.GET.get('date')
    selected_lesson = request.GET.get('lesson')
    all_groups = Users.objects.values_list('group', flat=True).distinct()
    if selected_date and selected_lesson:
        present_student_ids = Attendance.objects.filter(
            lesson=selected_lesson,
            datetime__date=selected_date,
            marked=1
        ).values_list('student_id', flat=True)
    else:
        present_student_ids = []
    if selected_group:
        students = Users.objects.filter(group=selected_group).order_by('name')
    else:
        students = Users.objects.none()
    context = {'students': students, 'selected_group': selected_group,
               'selected_date': selected_date, 'all_groups': all_groups, 'selected_lesson': selected_lesson, 'present_student_ids': present_student_ids}
    return render(request, 'attendance/attendance_list.html', context)

def view_attendance(request):
    if request.method == 'POST':
        lesson = request.POST.get('lesson')
        present_ids = request.POST.getlist('present_students')
        present_date = request.POST.get('present_date')
        selected_group = request.POST.get('group')
        students = Users.objects.filter(group=selected_group).order_by('name')
        for student in students:
            if str(student.id) in present_ids:
                status = 1
            else:
                status = 0
            Attendance.objects.create(lesson=lesson, student_id=student.id, datetime=present_date, marked=status)
        return redirect(f'/attendance/?group={selected_group}')