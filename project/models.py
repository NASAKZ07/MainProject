from django.conf import settings
from django.db import models
from django.utils import timezone

class User(models.Model):
    name = models.TextField()
    surname = models.TextField()
    password = models.TextField()
    telephone = models.TextField()

