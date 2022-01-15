from rest_framework.response import Response
from .models import Settings
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from .serializer import settingsSerializer

@api_view(["GET"])
def list(request):
    sett=Settings.objects.all()
    serialized=settingsSerializer(sett,many=True)
    return Response(serialized.data)

@api_view(["GET"])
def initial(request):
    settData={
        "setID":2201,
        "Name":"book return period",
        "value":"15"
    }
    serialized=settingsSerializer(data=settData)
    if serialized.is_valid():
        serialized.save()
        return Response({"Detail":"Settings value saved successfully"})
    else:
        return Response({"Detail":"sorry some error occured or else you have already run the api."})

@api_view(['PUT'])
def update(request,code):
    sett=get_object_or_404(klass=Settings,setID=code)
    settData=request.data.copy()
    settData['setID']=code
    serialized=settingsSerializer(sett,data=settData)
    if serialized.is_valid():
        serialized.save()
        return Response({"Detail":"Settings value changed successfully"})
    else:
        return Response({"Detail":"Oops sorry some error occured"})