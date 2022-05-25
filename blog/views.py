from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.

def blog(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'blog/blog.html',context)

def blog_single(request,pid):
    post = get_object_or_404(Post,pk=pid)
    context = {'post': post}
    return render(request, 'blog/blog-single.html',context)
