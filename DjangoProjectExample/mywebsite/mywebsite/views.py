from django.http import HttpResponse
from django.shortcuts import render


def homePage(request):
    data={
        'title': 'Home Page',
        'course_list': ['Java','PHP','Python'],
        'student_details': [
            {'name': 'Nick', 'phone': 12345678},
            {'name': 'Sam', 'phone': 98765432}
        ]
    }
    return render(request,"index.html",data)

def aboutUs(request):
    return HttpResponse("Welcome to mywebsite")

def Course(request):
    return HttpResponse("Welcome to Courses")

def CourseDetails(request,courseid):
    return HttpResponse(courseid)