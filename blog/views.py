from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView)
from .models import Post


# def index(request):
#     posts = Post.objects.order_by('-date_posted')
#     context = {
#         'posts': posts
#     }
#     return render(request, 'blog/index.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'subtitle', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



def about(request):
    context = {}
    return render(request, 'blog/about.html', context)


def posts(request):
    context = {}
    return render(request, 'blog/posts.html', context)


def contact(request):
    context = {}
    return render(request, 'blog/contact.html', context)