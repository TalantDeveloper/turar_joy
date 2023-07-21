from django.shortcuts import render
from .models import Faculties, Application


def home_view(request):
    faculties = Faculties.objects.all()

    print(request.POST.get('first_name'))
    print(request.POST.get('last_name'))
    print(request.POST.get('birthday'))
    print(request.POST.get('gender'))
    print(request.POST.get('email'))
    print(request.POST.get('phone'))
    print(request.POST.get('fakultet'))
    print(request.POST.get('image'))

    print(request.POST.get('subject'))

    content = {
        'faculties': faculties,
    }
    return render(request, 'main/home.html', content)
