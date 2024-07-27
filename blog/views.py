from django.shortcuts import render
from django.iews import generic
from .model import Post


class PostList(generic.ListView):
    model = Post 
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = name 'index.html'
    paginate_by = 6
    

