from django.shortcuts import render
from .models import BlogPost


# Create your views here.
def index(request):
    posts = BlogPost.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'pages/index.html', context)


def about(request):
    context = {}
    return render(request, 'pages/about.html', context)


def posts(request):
    context = {}
    return render(request, 'pages/posts.html', context)


def contact(request):
    context = {}
    return render(request, 'pages/contact.html', context)