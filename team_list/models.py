from django.db import models


# Create your models here.
class Team(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    dt = models.CharField(max_length=100, null=False)
    agno_fundacion = models.CharField(max_length=100, null=False)
    historia = models.TextField(max_length=500, null=False)
