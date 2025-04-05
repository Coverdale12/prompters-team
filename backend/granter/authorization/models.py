from django.db import models

class User(models.Model):
    username = models.CharField(max_length=16)
    name = models.CharField(max_length=32)
    telegram_id = models.IntegerField(null=True)
    email = models.EmailField()
    password = models.CharField(max_length=32)
    role = models.CharField(max_length=16)
    avatar = models.ImageField(null=True)
