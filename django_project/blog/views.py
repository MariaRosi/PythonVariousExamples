
from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {'author': 'Maria Rosi',
     'title': 'Blog Post 1',
     'content': 'First Post Content',
     'date_posted': '15 Feb, 2024'
     },
    {'author': 'Imtiaz Ahmed',
     'title': 'Blog Post 2',
     'content': 'Second Post Content',
     'date_posted': '16 Feb, 2024'
     }
]

def home(request):
    context = {
        'posts': posts
    }
    #return HttpResponse('<h1>Blog Home</h1>')
    return render(request, 'blog/home.html', context)

def about(request):
    #return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})


