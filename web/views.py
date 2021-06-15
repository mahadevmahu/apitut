from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def web(request):
    posts = Post.objects.all()
    
    return render(request,'dashboard.html',{"posts":posts})