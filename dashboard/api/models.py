from django.db import models

class Settings(models.Model):
    setID=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=20)
    value=models.CharField(max_length=20)
