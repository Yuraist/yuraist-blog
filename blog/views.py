# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import CommentForm


def blog_page(request):
    posts = Post.objects.order_by('-publication_date')
    return render(request, 'blog/blog.html', {'posts': posts})


def detail_post_page(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('detail_post_page', pk=post.pk)

    return render(request, 'blog/add_comment_to_post.html',
                      {'form': form})
