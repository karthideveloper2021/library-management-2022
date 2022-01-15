from rest_framework.response import Response
from .models import Settings
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

@api_view(['PUT'])
def settingsParameters(request,code,val):
    sett=get_object_or_404(klass=Settings,setID=code)
    sett.value=val
    sett.save()
    return Response({"Detail":"Settings value changed successfully"})
