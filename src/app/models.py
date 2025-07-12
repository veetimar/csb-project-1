from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=100)

class Message(models.Model):
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.TextField()
