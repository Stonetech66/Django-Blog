from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
# Create your views here.
from .models import Post
from django.urls import reverse_lazy

class PostListview(ListView):
	model= Post
	template_name= "blog/post_list.html"


class PostDetailView(DetailView):
	model= Post
	template_name= 'blog/post_detail.html'


class PostUpdateView(UpdateView):
	template_name= 'blog/post_update.html'
	model= Post
	fields= "__all__"
	success_url= reverse_lazy('blog:all')

class PostDeleteView(DeleteView):
	model= Post
	template_name= 'blog/post_delete.html'
	success_url= reverse_lazy('blog:all')

class PostCreateView(CreateView):
	model= Post
	fields= "__all__"
	template_name= 'blog/post_create.html'
	success_url= reverse_lazy('blog:all')
