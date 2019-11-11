from django.shortcuts import render
from .models import Blog


def blog(request):
    """ creating the blog view, ordering them by date created and rendering them on blogs.html"""
    blogs = Blog.objects.all().order_by('-date_created')
    return render(request, 'blog/blog.html', {'blogs': blogs})

