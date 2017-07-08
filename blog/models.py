# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.name


class Post(models.Model):
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=120, blank=True)
    image_url = models.CharField(max_length=300, blank=True)
    text = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)

    tags = models.ManyToManyField(Tag, blank=True)
    next_post = models.ForeignKey('self', null=True, blank=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return u'%s' % self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=datetime.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
