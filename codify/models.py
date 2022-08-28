from django.db import models


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=128)
    mentor_name = models.CharField(max_length=128)
    language = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=128)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    laptop = models.CharField(max_length=128)

    def __str__(self):
        return self.name
