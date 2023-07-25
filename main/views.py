from django.shortcuts import render, redirect
from .models import Faculties, Application
from .forms import ApplicationForm


def home_view(request):
    faculties = Faculties.objects.all()
    if request.method == 'POST':
        print(request.POST.get('full_name'))
    # message = ''
    #
    # if request.method == 'POST':
    #     faculty = Faculties.objects.get(link_name=request.POST.get('fakultet'))
    #     birthday = '1999-11-06'
    #     application = Application.objects.create(full_name=request.POST.get('full_name'),
    #                                              birthday=birthday,
    #                                              gender=request.POST.get('gender'),
    #                                              email=request.POST.get('email'),
    #                                              phone_number=request.POST.get('phone_number'),
    #                                              faculty=faculty,
    #                                              course=request.POST.get('kurs'),
    #                                              image=request.FILES.get('image'),
    #                                              i_va_ii=request.FILES.get('i_va_ii'),
    #                                              temir_daftar=request.FILES.get('temir_daftar'),
    #                                              yetim=request.FILES.get('yetim')
    #                                              )
    #     try:
    #         application.save()
    #         return redirect('/admin')
    #     except:
    #         return redirect('/')
    content = {
        'faculties': faculties,
    }
    return render(request, 'main/list.html', content)


def index_view(request):
    faculties = Faculties.objects.all()
    content = {
        'faculties': faculties,
    }
    return render(request, 'main/index.html', content)
