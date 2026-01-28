from django.shortcuts import render, redirect
from .models import *
from main.forms import DirectionsForm, SubjectForm, TeacherForm


# Create your views here.

def home_page_view(request):
    return render(request, 'home.html')

def directions_view(request):
    form = DirectionsForm()
    if request.method == 'POST':
        form = DirectionsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('directions')

    directions = Direction.objects.order_by('name')

    context = {
        'directions': directions,
        'form': form
    }
    return render(request, 'directions.html', context)

def direction_view(request, pk):
    direction = Direction.objects.get(id=pk)

    context = {
        'direction': direction,
    }
    return render(request, 'direction-details.html', context)

def subjects_view(request):
    form = SubjectForm()
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('subjects')

    subjects = Subject.objects.order_by('name')

    context = {
        'subjects': subjects,
        'form': form
    }
    return render(request, 'subjects.html', context)

def subject_view(request, pk):
    subject = Subject.objects.get(id=pk)

    context = {
        'subject': subject,
    }
    return render(request, 'subject-details.html', context)

def teachers_view(request):
    form = TeacherForm()
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('teachers')

    teachers = Teacher.objects.all().order_by('name')

    context = {
        'teachers': teachers,
        'form': form
    }
    return render(request, 'teachers.html', context)

def teacher_view(request, pk):
    teacher = Teacher.objects.get(id=pk)

    context = {
        'teacher': teacher,
    }
    return render(request, 'teacher-details.html', context)