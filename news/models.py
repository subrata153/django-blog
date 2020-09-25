from django.db import models

# Create your models here.

class News(models.Model):
    name = models.CharField(max_length=500,default='-')
    short_txt = models.TextField(default='-')
    body_txt = models.TextField(default='-')
    date = models.CharField(max_length=12)
    time = models.CharField(max_length=20, default='00:00:00')
    picname = models.TextField(default='-')
    picurl= models.TextField(default='-')
    author = models.CharField(max_length=50,default='-')
    catname = models.CharField(max_length=50,default='-')
    catid = models.IntegerField(default=0)
    ocatid = models.IntegerField(default=0)
    show = models.IntegerField(default=0)
    tag = models.TextField(default='')

    def __str__(self):
        return self.name


class TrendingNews(models.Model):
    tnews = models.CharField(max_length=200,default='-')

    def __str__(self):
        return self.tnews