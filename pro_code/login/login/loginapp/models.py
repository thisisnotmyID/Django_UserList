from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null = False,max_length=10)
    password = models.CharField(null=False,max_length=10)
