# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 06:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagedetails',
            name='colors',
            field=models.ManyToManyField(related_name='_imagedetails_colors_+', to='application.ImageDetails'),
        ),
    ]