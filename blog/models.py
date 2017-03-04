# -*- coding: utf-8 -*-
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=120, blank=True)
    image_url = models.CharField(max_length= 300, blank=True)
    text = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return u'%s' % self.title
