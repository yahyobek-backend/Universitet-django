from django.shortcuts import render, redirect, get_object_or_404
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

def update_direction_view(request, pk):
    direction = get_object_or_404(Direction, id=pk)
    if request.method == 'POST':
        direction.name = request.POST.get('name')
        direction.is_active = request.POST.get('is_active') == 'on'
        direction.save()
        return redirect('directions')
    context = {
        'direction': direction,
    }
    return render(request, 'direction-update.html', context)

def direction_delete_confirmation_view(request, pk):
    direction = get_object_or_404(Direction, id=pk)

    context = {
        'direction': direction,
    }
    return render(request, 'direction-confirmation.html', context)

def direction_delete_view(request, pk):
    direction = get_object_or_404(Direction, id=pk)
    direction.delete()
    return redirect('directions')

def subjects_view(request):
    form = SubjectForm()
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('subjects')

    subjects = Subject.objects.order_by('name')

    search = request.GET.get('search')
    if search is not None:
        subjects = Subject.objects.filter(name__contains=search)

    context = {
        'subjects': subjects,
        'form': form,
        'search': search,
    }
    return render(request, 'subjects.html', context)

def subject_view(request, pk):
    subject = Subject.objects.get(id=pk)

    context = {
        'subject': subject,
    }
    return render(request, 'subject-details.html', context)

def update_subject_view(request, pk):
    subject = get_object_or_404(Subject, id=pk)
    if request.method == 'POST':
        subject.name = request.POST.get('name')
        subject.is_main = request.POST.get('is_main') == 'on'
        subject.direction = get_object_or_404(Direction, id=request.POST['direction_id'])
        subject.save()
        return redirect('subjects')

    directions = Direction.objects.all().order_by('name')

    context = {
        'subject': subject,
        'directions': directions,
    }
    return render(request, 'subject-update.html', context)

def subject_delete_view(request, pk):
    subject = get_object_or_404(Subject, id=pk)
    subject.delete()
    return redirect('subjects')

def teachers_view(request):
    form = TeacherForm()
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('teachers')

    teachers = Teacher.objects.all().order_by('name')

    search = request.GET.get('search')
    if search is not None:
        teachers = Teacher.objects.filter(name__contains=search)

    context = {
        'teachers': teachers,
        'form': form,
        'search': search,
    }
    return render(request, 'teachers.html', context)

def teacher_view(request, pk):
    teacher = Teacher.objects.get(id=pk)

    context = {
        'teacher': teacher,
    }
    return render(request, 'teacher-details.html', context)

def teacher_update_view(request, pk):
    teacher = get_object_or_404(Teacher, id=pk)
    if request.method == 'POST':
        teacher.name = request.POST.get('name')
        teacher.age = request.POST.get('age')
        teacher.gender = request.POST.get('gender')
        teacher.level = request.POST.get('level')
        teacher.subject = get_object_or_404(Subject, id=request.POST.get('subject_id'))
        teacher.save()
        return redirect('teachers')
    subjects = Subject.objects.all().order_by('name')

    context = {
        'teacher': teacher,
        'subjects': subjects,
    }
    return render(request, 'teacher-update.html', context)

def teacher_confirmation_view(request, pk):
    teacher = get_object_or_404(Teacher, id=pk)

    context = {
        'teacher': teacher,
    }
    return render(request, 'teacher-confirmation.html', context)

def teacher_delete_view(request, pk):
    teacher = get_object_or_404(Teacher, id=pk)
    teacher.delete()
    return redirect('teachers')