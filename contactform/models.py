from django.db import models

# Create your models here.
class ContactForm(models.Model):

    name = models.CharField(max_length=50)
    email = models.TextField(default='-')
    message = models.TextField(default='-')
    date = models.CharField(max_length=50,default='-')
    time = models.CharField(max_length=50,default='-')

    def __str__(self):
        return self.name