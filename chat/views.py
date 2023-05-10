from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .forms import CommentForm

def home(request):
    posts = Post.objects.all()
    return render(request, 'chat/home.html', {'posts':posts})

def details(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method =='POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('details', slug=post.slug)
        
    else:
        form = CommentForm()
    return render(request, 'chat/details.html', {'post':post, 'form':form})

# Create your views here.
