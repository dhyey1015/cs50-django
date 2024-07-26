from django.db import models

# Create your models here.

class Fligth(models.Model):
    origin = models.TextField(max_length= 100)
