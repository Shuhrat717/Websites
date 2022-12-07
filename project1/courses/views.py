from django.shortcuts import render
from .models import Courses


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def courses(request):
    posts = Courses.objects.filter(is_published=True)
    context = {
        'posts': posts
    }
    return render(request, 'courses.html', context)


def courses_detail(request, pk):
    post = Courses.objects.get(idx=pk)
    context = {
        'post': post
    }

    return render(request, 'courses_detail.html', context)


