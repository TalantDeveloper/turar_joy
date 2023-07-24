from django.shortcuts import render
from .models import Faculties, Application
from .forms import ApplicationForm


def home_view(request):
    faculties = Faculties.objects.all()
    print(request.POST.get('full_name'))
    print(request.POST.get('birthday'))
    print(request.POST.get('gender'))
    print(request.POST.get('email'))
    print(request.POST.get('phone_number'))
    print(request.POST.get('fakultet'))
    print(request.POST.get('image'))
    print(request.POST.get('kurs'))
    print(request.FILES.get('image'))
    if request.method == 'POST':
        application = ApplicationForm(request.POST, request.FILES)
        if application.is_valid():
            pass
    content = {
        'faculties': faculties,
    }
    return render(request, 'main/home.html', content)
