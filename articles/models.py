from django.db import models

class articleModel(models.Model):
    title = models.CharField(max_length=100)