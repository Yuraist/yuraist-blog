from django.shortcuts import render, render_to_response
from blog.models import Post

def main(request):
    posts = Post.objects.order_by('-publication_date')
    last_posts = posts[:4]
    return render(request, 'blog/main.html', {
        'posts': posts,
        'last_posts': last_posts,
    })

def robots(request):
    return render_to_response('blog/robots.txt', content_type="plain/text")
