from django.shortcuts import render


def home(request):
    value = 'мои поздравления, все работает!'
    return render(request, 'home.html', {'value': value})