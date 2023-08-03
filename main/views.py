from django.shortcuts import render, redirect
from .models import Faculties, Application, Status
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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
                                                 yetim=request.FILES.get('yetim'),
                                                 yoshlar_daftar=request.FILES.get('yoshlar_daftar'),
                                                 oila_i_va_ii=request.FILES.get('oila_i_va_ii'),
                                                 boshqa=request.FILES.get('boshqa'),
                                                 status=Status.objects.get(pk=1)
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


@login_required(login_url='account:login')
def home_view(request):
    faculties = Faculties.objects.all()
    applications = Application.objects.all()
    status = Status.objects.all()
    content = {
        'faculties': faculties,
        'applications': applications,
        'hammasi': len(applications),
        'qabul': len(Application.objects.filter(status_id=2)),
        'radetildi': len(Application.objects.filter(status_id=3)),
        'korilmaganlar': len(Application.objects.filter(status_id=1)),
    }
    return render(request, 'main/list.html', content)


@login_required(login_url='account:login')
def update_view(request, pk):
    application = Application.objects.get(pk=pk)
    status = Status.objects.all()
    if request.method == 'POST':
        statu = Status.objects.get(pk=request.POST.get('status'))
        print(statu)
        application.status = statu
        application.save()
        return redirect('main:home')
    content = {
        'application': application,
        'status': status,
    }
    return render(request, 'main/update.html', content)


def status_view(request, pk):
    status = Status.objects.get(pk=pk)
    applications = Application.objects.filter(status=status)
    faculties = Faculties.objects.all()
    content = {
        'faculties': faculties,
        'applications': applications,
        'status': status
    }
    return render(request, 'main/list.html', content)


# def qabul_view(request):
#     applications = Application.objects.filter(is_qabul=True)
#     content = {
#         'faculties': faculties,
#         'applications': applications,
#         'qabuls': qabuls,
#         'radetilgan': radetilgan,
#         'hammasi': hammasi,
#         'notsees': notsees
#     }
#     return render(request, 'main/list.html', content)
