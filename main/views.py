from django.shortcuts import render
from .models import Blog

def mainindex(request):
    noti = Blog.objects.all()
    return render(request, 'main/index.html', {'noti':noti})