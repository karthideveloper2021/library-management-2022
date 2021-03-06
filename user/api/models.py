from django.db import models

class User(models.Model): 
    Name=models.CharField(max_length=50)
    regNo=models.IntegerField()
    year=models.IntegerField()
    borrowDate=models.DateTimeField(editable=False,auto_now_add=True)
    returnDate=models.DateTimeField()
    bookNo=models.IntegerField()
    returnStatus=models.BooleanField(default=False)


