from django.conf.urls import include, url
from django.contrib import admin
from .views import main, robots
from authentification.views import login_user, registration, logout_user
from editor.views import create_post

urlpatterns = [
    # Examples:
    # url(r'^$', 'yuraist.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', main, name='main'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^info/', include('info.urls')),
    url(r'^login/$', login_user, name='login_user'),
    url(r'^registration/$', registration, name='registration'),
    url(r'^logout/$', logout_user, name='logout_user'),
    url(r'^create/$', create_post, name='create_post'),
    url(r'^robots.txt$', robots),
]
