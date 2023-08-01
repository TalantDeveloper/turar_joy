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
        request.session['ariza'] = {'name': application.full_name, 'id': application.id}
        return redirect('main:success')
    content = {
        'faculties': faculties,
    }
    return render(request, 'main/index.html', content)


def success_view(request):
    return render(request, 'main/success.html')


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
    hammasi = len(applications)
    qabuls = len(Application.objects.filter(is_qabul=True))
    radetilgan = len(Application.objects.filter(is_radetildi=True))
    notsees = hammasi - qabuls - radetilgan

    content = {
        'faculties': faculties,
        'applications': applications,
        'qabuls': qabuls,
        'radetilgan': radetilgan,
         'hammasi': hammasi,
        'notsees': notsees
    }
    return render(request, 'main/list.html', content)


def update_view(request, pk):
    application = Application.objects.get(pk=pk)
    if request.method == 'POST':
        qabul = request.POST.get('qabul')
        if qabul == 'qabul':
            application.is_qabul = True
        else:
            application.is_radetildi = True
        application.save()
        return redirect('main:home')
    content = {
        'application': application
    }
    return render(request, 'main/update.html', content)

