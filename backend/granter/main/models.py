from django.db import models

from authorization.models import Profile


class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=32)
    short_name = models.CharField(max_length=32, null=True, blank=True)
    region = models.CharField(max_length=32)
    industry = models.CharField(max_length=32)

    def __str__(self):
        return self.full_name


class Startup(models.Model):
    STATUS_CHOICES = [
        ('waiting', 'Waiting'),
        ('inprogress', 'In Progress'),
        ('done', 'Done'),
    ]

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='waiting')
    region = models.CharField(max_length=32, null=True, blank=True)
    industry = models.CharField(max_length=32, null=True, blank=True)
    direction = models.CharField(max_length=32, null=True, blank=True)
    budget = models.FloatField(null=True, blank=True)
    publish_date = models.DateField()
    finish_date = models.DateField()
    days = models.IntegerField()

    def __str__(self):
        return self.name
    
    
class OrganizationHasUser(models.Model):
    ROLE_CHOICES = [
        ('owner', 'Owner'),
        ('participant', 'Participant'),
    ]

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    role = models.CharField(max_length=16, choices=ROLE_CHOICES)

    class Meta:
        unique_together = ('organization', 'user')



    
class Investor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()

# Create your models here.
