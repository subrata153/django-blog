from __future__ import unicode_literals
from django.db import models
# from django.db.models import Model 
# from django.db.models import Model 

# Create your models here.
# models.IntegerField()
# models.CharField()

class Main(models.Model):

    name = models.CharField(max_length=30)
    about = models.TextField()
    abouttxt = models.TextField(default='-')
    facebook = models.URLField(default='-')
    twitter = models.URLField(default='-')
    youtube = models.URLField(default='-')
    set_name = models.CharField(default='Settings',max_length=30)
    tel = models.CharField(default='00000',max_length=30)
    footer_link = models.URLField(default='-')

    picname = models.TextField(default="")
    picurl = models.TextField(default="")

    picname2 = models.TextField(default="")
    picurl2 = models.TextField(default="")

    def __str__(self):
        return self.set_name

# class News(models.Model):



