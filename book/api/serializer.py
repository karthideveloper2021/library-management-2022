from rest_framework import serializers
from user.api.models import User
from .models import Book

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
            'bookStock','bookIssued','bookAvailable','created','modified')

class BookSerializerStore(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"

class BookSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=['Name','author','date_of_pub','description',
            'bookStock']