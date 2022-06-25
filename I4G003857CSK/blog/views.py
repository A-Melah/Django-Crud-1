from django.shortcuts import render

# Create your views here.
from winreg import DeleteValue
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from .models import Post

class PostListView(generic.ListView):
    model = Post


class PostCreateView(CreateView):

    model = Post
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')


class PostDetailView(DetailView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')


class PostDeleteView(DeleteView):
    model = Post
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')


