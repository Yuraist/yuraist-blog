from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.blog_page, name='blog_page'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail_post_page, name='detail_post_page'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
]
