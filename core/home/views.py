from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    people = [
        {'name': 'Dev', 'age': 15},
        {'name': 'Rick', 'age': 25},
        {'name': 'Seema', 'age': 17},
        {'name': 'Sally', 'age': 45},
        {'name': 'Umair', 'age': 20}
    ]

    # return HttpResponse('This is the home page')
    return render(request, 'index.html', context={'page': 'Home', 'people': people})


def about(request):
    return render(request, 'about.html', context={'page': 'About'})


def contact(request):
    return render(request, 'contact.html', context={'page': 'Contact'})
