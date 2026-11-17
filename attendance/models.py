from django.db import models

class Users(models.Model):
    name = models.CharField(max_length = 100)
    role =  [("s", "student"),
             ("t", "teacher"),]
    login = models.CharField(max_length = 10)
    password = models.CharField(max_length = 10)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    lesson = models.CharField(max_length = 10)
    student = models.ForeignKey(Users, on_delete=models.CASCADE)
    marked = models.BooleanField()
    datetime = models.DateTimeField()

    def __str__(self):
        return f"{self.student.name} - {self.lesson} {str(self.datetime)}"
    
