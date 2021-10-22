from django.db import models
from django.contrib.auth.models import User
import uuid

from django.db.models.fields import TextField


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return self.name


class Skill(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    descrition = models.TextField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)


    def __str__(self):
        return self.name

class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True,related_name='receiver')
    subject = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.subject