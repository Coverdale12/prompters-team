from django.db import models

class Profile(models.Model):
    username = models.TextField()
    name = models.TextField()
    telegram_id = models.IntegerField(null=True)
    email = models.EmailField()
    password = models.TextField()
    role = models.TextField()
    avatar = models.ImageField(null=True)
