from rest_framework import fields, serializers
from rest_framework import serializers
from .models import Book,User

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields= "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"


