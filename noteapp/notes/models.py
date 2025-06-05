from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):
    user = models.ForeignKey(to=User, related_name="user", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
