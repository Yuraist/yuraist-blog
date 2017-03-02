from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^about/$', views.about_page, name='about_page'),
    url(r'^contact/$', views.contact_page, name='contact_page'),
]
