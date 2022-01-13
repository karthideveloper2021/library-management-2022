from django.shortcuts import get_object_or_404, redirect,Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import BookSerializer, BookSerializerStore,UserSerializer, UserSerializerStore
from django.db.models import F
from .models import Book,User

@api_view(['GET'])
def apiIndex(request):
    book=Book.objects.filter(serial=100)[0]
    print(type(book))
    print(book)
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
    print(serialized.data)
    finalSerializer=[]
    for item in serialized.data:
        if status==True and item['bookIssued']==0:
            finalSerializer.append(item)
        elif status==False and item['bookIssued']!=0:
            finalSerializer.append(item)
        
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
    


##~~ user api

@api_view(['GET'])
def userList(request):
    users=User.objects.all()
    serialized=UserSerializer(users,many=True)
    return Response(serialized.data)

@api_view(['GET'])
def userDetail(request,reg):
    user=get_object_or_404(klass=User,regNo=reg,returnStatus=False)
    serialized=UserSerializer(user,many=False)
    return Response(serialized.data)
        
@api_view(['GET'])
def userDetailRecords(request,reg):
    user=User.objects.filter(regNo=reg)
    if user.exists():
        serialized=UserSerializer(user,many=True)
        return Response(serialized.data)
    else:
        return Response({"Detail":"User not found.."})
   

@api_view(['POST'])
def userAdd(request):
    userAddData=request.data
    serialized=UserSerializerStore(data=userAddData)
    bkNo=userAddData['bookNo']
    try:
        user=User.objects.get(bookNo=bkNo,returnStatus=False)
        return Response({"Detail":"Book issued already"})
    except User.DoesNotExist:
        book=get_object_or_404(klass=Book,serial=bkNo)
        if serialized.is_valid():
            serialized.save()
            book.no_of_times_borrowed=F('no_of_times_borrowed')+1
            book.save()
        return redirect("user-list")

@api_view(['PUT'])
def userUpdate(request,reg,ser):
    user=get_object_or_404(klass=User,regNo=reg,bookNo=ser,returnStatus=False)
    serialized=UserSerializerStore(instance=user,data=request.data)
    if serialized.is_valid():
        serialized.save()
    return redirect("user-list")
    
@api_view(['POST'])
def userReturn(request,reg,ser,status):
    book = get_object_or_404(klass=User,bookNo=ser,regNo=reg,returnStatus=False)
    book.returnStatus=status
    book.save()
    return redirect("user-list")


@api_view(['DELETE'])
def userDelete(request,reg,ser):
    book=User.objects.filter(regNo=reg,bookNo=ser)
    if book.exists():
        book.delete()
        return redirect("user-list")
    else:
        return Response("user not found!!")