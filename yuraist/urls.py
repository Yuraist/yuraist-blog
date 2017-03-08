from django.conf.urls import include, url
from django.contrib import admin
from .views import main
from authentification.views import login, registration

urlpatterns = [
    # Examples:
    # url(r'^$', 'yuraist.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', main, name='main'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^info/', include('info.urls')),
    url(r'^login/$', login, name='login'),
    url(r'^registration/$', registration, name='registration'),
]
