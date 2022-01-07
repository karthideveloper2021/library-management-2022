from django.shortcuts import redirect
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import BookSerializer,UserSerializer
from .models import Book,User

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
    if User.objects.filter(regNo=reg).exists():
        user=User.objects.get(regNo=reg)
        serialized=UserSerializer(user,many=False)
        return Response(serialized.data)
    else:
        return Response("User doesn't exist")
        

@api_view(['POST'])
def userCreate(request):
    serialized=UserSerializer(data=request.data)
    # print(serialized)
    # print(serialized.is_valid())
    # if serialized.is_valid():
    #     serialized.save()
            
    bkNo=request.data['bookNo']
    # return redirect("user-list")

    if Book.objects.filter(serial=bkNo).exists():
        if serialized.is_valid():
            serialized.save()
            book=Book.objects.get(serial=bkNo)
            book.no_of_borrowed+=1
            book.save()
        return redirect('user-list')
    else:
        return Response("Book not found..")

    

@api_view(['DELETE'])
def userDelete(request,reg,ser):
    if User.objects.filter(regNo=reg).exists():
        book=User.objects.get(regNo=reg,bookNo=ser)
        book.delete()
        return redirect("user-list")
    else:
        return Response("user not found!!")