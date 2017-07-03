from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length = 50, unique = True)
    passwd = models.CharField(max_length = 20, default = 'jack')

