from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(null=True, blank=True,max_length=200)
    age = models.CharField(null=True, blank=True,max_length=200)