from django.core.checks import messages
from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class contact(models.Model):
    name = models.CharField(max_length=50)
    messages = models.CharField(max_length=120)