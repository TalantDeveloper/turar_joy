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
        return render(request, 'main/success.html', {
            'aplication': application
        })
    content = {
        'faculties': faculties,
    }
    return render(request, 'main/index.html', content)


def check_id(request):
    if request.method == 'POST':
        application_id = request.POST.get('id')
        application = Application.objects.get(id=application_id)
        return render(request, 'main/check.html', {'application': application})
    else:
        return render(request, 'main/check.html')


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

