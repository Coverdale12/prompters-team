from django.db import models

class Request(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    sender = models.CharField(max_length=20)
    reciever = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

    def __str__(self):
         return self.id


