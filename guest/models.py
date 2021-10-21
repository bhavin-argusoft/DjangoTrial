from django.db import models

class Guest(models.Model):

    name = models.CharField(max_length=100)
    phone = models.IntegerField(max_length=20)
    address = models.TextField(max_length=500)
    email = models.EmailField()