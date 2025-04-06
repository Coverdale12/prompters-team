from django.db import models
import uuid

class Profile(models.Model):
    username = models.TextField()
    name = models.TextField()
    telegram_id = models.IntegerField(null=True)
    email = models.EmailField(unique=True)
    password = models.TextField()
    role = models.TextField()
    avatar = models.ImageField(null=True)

class Token(models.Model):
    token = models.CharField(max_length=255, unique=True, default=uuid.uuid4)
    user_id = models.IntegerField()
    
    def __str__(self):
        return self.token
