from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

'''Create the Post view here'''

'''Build with class based views.'''

class HomeView(TemplateView):
    template_name = "home.html"

class PostListView(ListView):
    model = Post 
    template_name = "posts.html"

class PostDetailView(DetailView):
    model = Post 
    template_name = "detail.html"
    

class CreateStoryView(CreateView):
    model = Post
    fields = ['title', 'story', 'photo'] 
    template_name = "new_story.html"
    success_url = reverse_lazy("posts:home")
    
    def form_valid(self, form):
        form.instance.user_account = self.request.user
        return super().form_valid(form)

class UpdateStoryView(UpdateView):
    model = Post 
    fields = ['title', 'story', 'photo']
    template_name = "update_story.html"
    success_url = reverse_lazy("posts:home")

class DeleteStoryView(DeleteView):
    model = Post 
    template_name = "delete_story.html"
    success_url = reverse_lazy("posts:home")
