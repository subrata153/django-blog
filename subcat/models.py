from django.db import models

# Create your models here.

class Subcat(models.Model):
    name = models.CharField(max_length=50,default='-')
    catname = models.TextField(max_length=50,default='-')
    catid = models.IntegerField(default=0)
    description = models.TextField(max_length=500, default='-')

    def __str__(self):
        return self.name