from django.db import models


# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=1337)


class Women(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
