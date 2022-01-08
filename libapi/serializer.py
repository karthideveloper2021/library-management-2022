from rest_framework import fields, serializers
from rest_framework import serializers
from .models import Book,User

class BookSerializer(serializers.ModelSerializer):

    bookAvailable=serializers.SerializerMethodField('_BookAvaliable')
    bookIssued=serializers.SerializerMethodField('_BookIssued')

    def _BookAvaliable(self,book):
        ser=book.serial
        user=User.objects.filter(bookNo=ser,returnStatus=False)
        totalStock=getattr(book,'bookStock')
        bkavail=totalStock-len(user)
        return bkavail
    

    def _BookIssued(self,book):
        ser=book.serial
        bkIssue=len(User.objects.filter(bookNo=ser,returnStatus=False))
        return bkIssue

    class Meta:
        model=Book
        fields=('serial','Name','author',
            'date_of_pub','description','no_of_times_borrowed',
            'bookStock','bookIssued','bookAvailable')

class UserSerializer(serializers.ModelSerializer):
    bookName=serializers.SerializerMethodField("_bookname")

    def _bookname(self,user):
        ser=getattr(user,'bookNo')
        book=Book.objects.filter(serial=ser)
        bkName=book.values()[0]['Name']
        return bkName
    class Meta:
        model=User
        fields=('Name','regNo','year','bookNo',
        'bookName','borrowDate','returnDate','returnStatus')

