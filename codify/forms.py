from django import forms
from .models import Course, Student


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'  # Если все поля то __all__
        # fiels = ['name', 'mentor_name',]  # Если только некоторые поля


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
