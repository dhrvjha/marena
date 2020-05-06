from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from .models import posts

# Create your views here.

def searchView(request):
    full_path = request.get_full_path_info()
    full_path, query_string = full_path.split('=')
    return render(request, 'blog/search_result.html', { 'posts' : posts.objects.filter(title__startswith = query_string).order_by('-date_posted') })

class PostListView(ListView):
    model = posts
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = posts
    template_name = 'blog/detail.html'
    context_object_name = 'posts'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = posts
    template_name = 'blog/create.html'
    context_object_name = 'posts'
    fields = ['title','post_text']

    def form_valid(self, form):
        form.instance.author = self.request.user.username
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = posts
    template_name = 'blog/create.html'
    context_object_name = 'posts'
    fields = ['title','post_text']
    
    def test_func(self):
        post = self.get_object()
        if self.request.user.username == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = posts
    template_name = 'blog/delete.html'
    context_object_name = 'posts'
    fields = ['title','post_text']
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user.username == post.author:
            return True
        return False