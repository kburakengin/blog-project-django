from django.shortcuts import render


# Create your views here.
def index(request):
    context = {}
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