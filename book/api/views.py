from django.shortcuts import get_object_or_404, redirect,Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import BookSerializer, BookSerializerStore
from .models import Book

@api_view(['GET'])
def apiIndex(request):
    return Response()

##~~ book api

@api_view(['GET'])
def bookList(request):
    books=Book.objects.all()
    serialized=BookSerializer(books,many=True)
    return Response(serialized.data)

@api_view(['GET'])
def bookListReturn(request,status):
    books=Book.objects.all()
    serialized=BookSerializer(books,many=True)
    finalSerializer=[]
    
    def specificValues(item):
        finalData={}
        finalData['serial']=item['serial']
        finalData['Name']=item['Name']
        finalData['bookStock']=item['bookStock']
        finalData['bookIssued']=item['bookIssued']
        finalData['bookAvailable']=item['bookAvailable']
        return finalData

    for item in serialized.data:
        if status==True and item['bookIssued']!=0:
            finalSerializer.append(specificValues(item))
        elif status==False and item['bookIssued']==0:
            finalSerializer.append(specificValues(item))
        
    return Response(finalSerializer)

@api_view(['GET'])
def bookDetail(request,ser):
    book=get_object_or_404(klass=Book,serial=ser)
    serialized=BookSerializer(book,many=False)
    return Response(serialized.data)
        

@api_view(['POST'])
def bookCreate(request):
    bookAddData=request.data
    book=Book.objects.filter(serial=bookAddData['serial'])
    if not book.exists():
        serialized=BookSerializerStore(data=bookAddData)
        if serialized.is_valid():
            serialized.save()
        return redirect('book-list')
    else:
        return Response({"Detail":"Another book exist with same serial number."},status=201)

@api_view(['DELETE'])
def bookDelete(request,ser):
    book=get_object_or_404(klass=Book,serial=ser)
    book.delete()
    return redirect("book-list")

@api_view(['PUT'])
def bookUpdate(request,ser):
    book=get_object_or_404(klass=Book,serial=ser)
    serialized=BookSerializerStore(instance=book,data=request.data)
    if serialized.is_valid():
        serialized.save()
    return redirect("book-list")
    
