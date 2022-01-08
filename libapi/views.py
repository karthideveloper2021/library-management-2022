from django.shortcuts import redirect
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import BookSerializer,UserSerializer
from django.db.models import F
from .models import Book,User

@api_view(['GET'])
def apiIndex(request):
    return Response()

##~~ book api

@api_view(['GET'])
def bookList(request):
    books=Book.objects.all()
    print(books)
    serialized=BookSerializer(books,many=True)
    return Response(serialized.data)

@api_view(['GET'])
def bookDetail(request,ser):
    if Book.objects.filter(serial=ser).exists():
        book=Book.objects.get(serial=ser)
        serialized=BookSerializer(book,many=False)
        return Response(serialized.data)
    else:
        return Response("Data doesn't exist")
        

@api_view(['POST'])
def bookCreate(request):
    serialized=BookSerializer(data=request.data)
    if serialized.is_valid():
        serialized.save()
    return redirect('book-list')

@api_view(['DELETE'])
def bookDelete(request,ser):
    book=Book.objects.get(serial=ser)
    book.delete()
    return redirect("book-list")

##~~ user api

@api_view(['GET'])
def userList(request):
    users=User.objects.all()
    serialized=UserSerializer(users,many=True)
    return Response(serialized.data)

@api_view(['GET'])
def userDetail(request,reg):
    user=User.objects.filter(regNo=reg,returnStatus=False)
    if user.exists():
        serialized=UserSerializer(user,many=True)
        return Response(serialized.data)
    else:
        return Response("User doesn't exist")
        

@api_view(['POST'])
def userAdd(request):
    serialized=UserSerializer(data=request.data)
    bkNo=request.data['bookNo']
    book=Book.objects.filter(serial=bkNo)
    if book.exists():
        if serialized.is_valid():
            serialized.save()
            book.update(no_of_times_borrowed=F('no_of_times_borrowed')+1)
        return redirect('user-list')
    else:
        return Response("Book not found..")

@api_view(['PUT'])
def userUpdate(request,reg,ser):
    user=User.objects.filter(regNo=reg,bookNo=ser,returnStatus=False)
    if user.exists():
        serialized=UserSerializer(instance=user,data=request.data)
        if serialized.is_valid():
            serialized.save()
    else:    
        return Response("user not exists...")
    

def userReturn(request,reg,ser,status):
    book=User.objects.filter(regNo=reg,bookNo=ser,returnStatus=False)
    if book.exists():
        book.update(returnStatus=status)
        return redirect("user-list")
    else:
        return Response("user not found!!")

@api_view(['DELETE'])
def userDelete(request,reg,ser):
    book=User.objects.filter(regNo=reg,bookNo=ser)
    if book.exists():
        book.delete()
        return redirect("user-list")
    else:
        return Response("user not found!!")