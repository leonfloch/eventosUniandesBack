from django.db import models
from django.utils import timezone
import uuid

# Create your models here.

class User(models.Model):
    username = models.CharField(primary_key=True, max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username

class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event_name = models.CharField(max_length=200)
    event_category = models.CharField(max_length=200)
    event_place = models.CharField(max_length=200)
    event_address = models.CharField(max_length=200)
    event_initial_date = models.DateTimeField(default=timezone.now)
    event_final_date = models.DateTimeField(default=timezone.now)
    event_type = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.event_name



class Authentication(models.Model):
    username = models.CharField(max_length=200)
    token = models.CharField(primary_key=True, max_length=200)

    def __str__(self):
        return self.token
