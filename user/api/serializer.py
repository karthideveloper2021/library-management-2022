from rest_framework import serializers
from .models import User
from book.api.models import Book

class UserSerializerStore(serializers.ModelSerializer):
        class Meta:
            model=User
            fields="__all__"

class UserSerializer(serializers.ModelSerializer):
    bookName=serializers.SerializerMethodField("_bookname")

    def _bookname(self,user):
        ser=getattr(user,'bookNo')
        book=Book.objects.get(serial=ser)
        bkName=getattr(book,'Name')
        return bkName
    class Meta:
        model=User
        fields=('Name','regNo','year','bookNo',
        'bookName','borrowDate','returnDate','returnStatus')

