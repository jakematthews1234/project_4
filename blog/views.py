from django.shortcuts import render
from .models import Blog


def blog(request):
    blogs = Blog.objects.all().order_by('-date_created')
    return render(request, 'blog/blog.html', {'blogs': blogs})

