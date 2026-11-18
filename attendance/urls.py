from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_student, name='attendance_list'),
    path('save/', views.view_attendance, name='save_attendance'),
]