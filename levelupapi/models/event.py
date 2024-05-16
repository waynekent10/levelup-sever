from django.db import models


class Event(models.Model):
    
    uid = models.CharField(max_length=50)
    bio = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    organizer = models.CharField(max_length=50)