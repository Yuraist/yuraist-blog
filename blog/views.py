from django.shortcuts import render, get_object_or_404
from .models import Post

def blog_page(request):
    posts = Post.objects.order_by('-publication_date')
    return render(request, 'blog/blog.html', {'posts': posts})

def detail_post_page(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})