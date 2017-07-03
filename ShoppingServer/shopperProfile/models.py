from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length = 50, unique = True)
    account = models.CharField(max_length = 50, unique = True)
    sex = models.CharField(max_length = 10)
    prefer_clothes = models.CharField(max_length = 50)
    prefer_pants = models.CharField(max_length = 50)
    prefer_books = models.CharField(max_length = 50)
    prefer_foods = models.CharField(max_length = 50)
    
class Budget(models.Model):
    userid = models.IntegerField(default=0)
    rest = models.IntegerField(default=0)
    upgradetime = models.IntegerField(default=0)
