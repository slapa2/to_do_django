from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=256)
    created = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(auto_now=True)
    done = models.BooleanField(default=False)