from django.shortcuts import render


def home_view(request):
    print(request.POST.get('first_name'))
    print(request.POST.get('last_name'))
    print(request.POST.get('birthday'))
    print(request.POST.get('gender'))
    print(request.POST.get('email'))
    print(request.POST.get('phone'))
    print(request.POST.get('fakultet'))
    print(request.POST.get('image'))

    print(request.POST.get('subject'))

    return render(request, 'main/home.html')
    pass
