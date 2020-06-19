from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView, UpdateView)
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


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'subtitle', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
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