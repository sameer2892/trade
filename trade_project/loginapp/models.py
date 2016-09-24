from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=10)
    password = models.CharField(max_length=30)




