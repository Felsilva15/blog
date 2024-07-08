# blog/views.py
from django.views.generic import ListView, DetailView
from .models import Post
from django.shortcuts import render

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

def about(request):
    return render(request, 'blog/about.html')
