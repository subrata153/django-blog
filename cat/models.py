from django.db import models

# Create your models here.

class Cat(models.Model):
    name = models.CharField(max_length=50,default='-')
    catname = models.CharField(max_length=50,default='uncat')
    catid = models.IntegerField(default=0)
    description = models.TextField(max_length=500,default='-')
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

