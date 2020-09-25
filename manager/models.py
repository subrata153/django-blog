from django.db import models

# Create your models here.
class Manager(models.Model):
    name = models.CharField(max_length=30)
    email = models.TextField(default='-')
    utxt = models.TextField(default='-')

    def __str__(self):
        return self.set_name