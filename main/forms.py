from django import forms
from .models import *

class DirectionsForm(forms.ModelForm):
    class Meta:
        model = Direction
        fields = '__all__'

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
