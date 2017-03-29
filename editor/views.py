from django.shortcuts import render, redirect
from blog.views import detail_post_page
from blog.models import Post
from datetime import datetime

def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        subtitle = request.POST['subtitle']
        img_url = request.POST['img-url']
        text = request.POST['post-text']
        publication_date = datetime.now()

        post = Post()
        post.title = title
        post.subtitle = subtitle
        post.image_url = img_url
        post.text = text
        post.publication_date = publication_date

        post.save()

        return redirect('detail_post_page', pk=post.pk)

    return render(request, 'editor/editor.html')
