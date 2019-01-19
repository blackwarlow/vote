from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Pool(models.Model):
    date = models.DateTimeField()
    name = models.CharField(max_length=100)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)

class Pool_variant(models.Model):
    variant_name = models.CharField(max_length=100)
    votes = models.IntegerField()
    belongs_to = models.ForeignKey(to=Pool, default='none', on_delete=models.CASCADE)

class Author(models.Model):
    name = models.CharField(max_length=100)
    social = models.CharField(max_length=100)
    role = models.CharField(max_length=20, default='developer')