from django.db import models

class Book(models.Model):
    serial=models.IntegerField(null=False,primary_key=True)
    Name=models.CharField(max_length=60)
    author=models.CharField(max_length=50)
    date_of_pub=models.DateField()
    description=models.CharField(max_length=250)
    no_of_times_borrowed=models.IntegerField(default=0)
    bookStock=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True,editable=False)
    modified=models.DateTimeField(auto_now=True)