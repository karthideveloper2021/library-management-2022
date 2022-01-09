from django.db import models

# Create your models here.

class Book(models.Model):
    serial=models.IntegerField(null=False,primary_key=True)
    Name=models.CharField(max_length=60)
    author=models.CharField(max_length=50)
    date_of_pub=models.DateField()
    description=models.CharField(max_length=250)
    no_of_times_borrowed=models.IntegerField(default=0)
    bookStock=models.IntegerField()


class User(models.Model): 
    Name=models.CharField(max_length=50)
    regNo=models.IntegerField()
    year=models.IntegerField()
    borrowDate=models.DateTimeField()
    returnDate=models.DateField()
    bookNo=models.IntegerField()
    returnStatus=models.BooleanField(default=False)

