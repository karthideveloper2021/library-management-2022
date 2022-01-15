from dataclasses import fields
from rest_framework import serializers
from .models import Settings

class settingsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Settings
        fields="__all__"
