from django.shortcuts import render
from .models import Users

def view_student(request):
    selected_group = request.GET.get('group')
    if selected_group:
        students = Users.objects.filter(group=selected_group).order_by('name')
    else:
        students = Users.objects.none()
    context = {'students': students, 'selected_group': selected_group}
    return render(request, 'attendance/attendance_list.html', context)