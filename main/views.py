from django.shortcuts import render, redirect
from .models import Faculties, Application
from django.contrib import messages


def welcome_view(request):
    faculties = Faculties.objects.all()
    if request.method == 'POST':
        faculty = Faculties.objects.get(link_name=request.POST.get('fakultet'))
        application = Application.objects.create(full_name=request.POST.get('name'),
                                                 birthday=request.POST.get('birthday'),
                                                 gender=request.POST.get('gender'),
                                                 email=request.POST.get('email'),
                                                 phone_number=request.POST.get('number'),
                                                 faculty=faculty,
                                                 course=request.POST.get('kurs'),
                                                 image=request.FILES.get('image'),
                                                 i_va_ii=request.FILES.get('nogiron'),
                                                 temir_daftar=request.FILES.get('temir'),
                                                 yetim=request.FILES.get('yetim')
                                                 )
        application.save()
        messages.success(request, f"{request.POST.get('name')}")
        return redirect('/')
    content = {
        'faculties': faculties,
    }
    return render(request, 'main/index.html', content)


def home_view(request):
    faculties = Faculties.objects.all()
    applications = Application.objects.all()
    content = {
        'faculties': faculties,
        'applications': applications,
    }
    return render(request, 'main/list.html', content)


def update_view(request, pk):
    application = Application.objects.get(pk=pk)
    content = {
        'application': application
    }
    return render(request, 'main/update.html', content)

