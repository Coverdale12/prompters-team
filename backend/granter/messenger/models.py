from django.db import models
from authorization.models import Profile
from main.models import Startup

class PrivateMessage(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(Profile, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(Profile, related_name='received_messages', on_delete=models.CASCADE)
    text = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'Message from {self.sender} to {self.recipient}'


class Topic(models.Model):
    id = models.AutoField(primary_key=True)
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name
    

class TopicMessage(models.Model):
    id = models.AutoField(primary_key=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField()
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'Message in topic {self.topic}'


class File(models.Model):
    FILE_TYPE_CHOICES = [
        ('file', 'File'),
        ('photo', 'Photo'),
        ('voice', 'Voice'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    data = models.BinaryField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=FILE_TYPE_CHOICES, default='file')

    def __str__(self):
        return self.name


class PrivateMessageHasFile(models.Model):
    private_message = models.ForeignKey(PrivateMessage, on_delete=models.CASCADE)
    file = models.ForeignKey(File, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('private_message', 'file')


class TopicMessageHasFile(models.Model):
    topic_message = models.ForeignKey(TopicMessage, on_delete=models.CASCADE)
    file = models.ForeignKey(File, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('topic_message', 'file')

class Notification(models.Model):
    NOTIFICATION_TYPE_CHOICES = [
        ('private', 'Private'),
        ('topic', 'Topic'),
        ('startup', 'Startup'),
    ]

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    got_at = models.DateTimeField(auto_now_add=True)
    is_sent = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)
    type = models.CharField(max_length=10, choices=NOTIFICATION_TYPE_CHOICES)
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    startup = models.ForeignKey(Startup, null=True, blank=True, on_delete=models.CASCADE)
    topic_message = models.ForeignKey(TopicMessage, null=True, blank=True, on_delete=models.CASCADE)
    private_message = models.ForeignKey(PrivateMessage, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'Notification for {self.user} - {self.title}'

# Create your models here.
