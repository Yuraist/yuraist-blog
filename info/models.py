from django.db import models

class Info(models.Model):
    author_fullname = models.CharField(max_length=100)
    author_description = models.TextField()
    #author_photo
    about_site = models.TextField()
    vk_url = models.URLField(default='https://www.facebook.com/yuraistom')
    fb_url = models.URLField(default='https://vk.com/yuraist')
    in_url = models.URLField(default='https://instagram.com/yuraist')
    tw_url = models.URLField(default='https://twitter.com/yuraist')
