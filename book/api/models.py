from django.db import models

class Book(models.Model):
   serial=models.IntegerField(primary_key=True)
   Name=models.CharField(max_length=50)
   author=models.CharField(max_length=30)
   date_of_pub=models.DateField()
   description=models.CharField(max_length=100)
   no_of_times_borrowed=models.IntegerField(default=0)
   bookStock=models.IntegerField()
   created=models.DateTimeField(auto_now_add=True)
   modified=models.DateTimeField(auto_now=True)
