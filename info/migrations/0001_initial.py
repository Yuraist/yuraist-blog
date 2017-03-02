# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author_fullname', models.CharField(max_length=100)),
                ('author_description', models.TextField()),
                ('about_site', models.TextField()),
                ('vk_url', models.URLField(default=b'www.facebook.com/yuraistom')),
                ('fb_url', models.URLField(default=b'vk.com/yuraist')),
                ('in_url', models.URLField(default=b'instagram.com/yuraist')),
                ('tw_url', models.URLField(default=b'twitter.com/yuraist')),
            ],
        ),
    ]
