# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from blog.models import Post


def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


class Project(models.Model):
    name = models.CharField(max_length=140)
    image = models.FileField(null=True, blank=True, upload_to=upload_location)
    description = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)

    authors = models.ManyToManyField(User)
    articles = models.ManyToManyField(Post)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u"%s" % self.name
