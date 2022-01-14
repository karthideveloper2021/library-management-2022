from datetime import timedelta
from django.shortcuts import get_object_or_404, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UserSerializer, UserSerializerStore
from django.db.models import F
from book.api.models import Book
from .models import User,Settings
from django.utils import timezone

@api_view(['GET'])
def userList(request):
    users=User.objects.all()
    serialized=UserSerializer(users,many=True)
    print(users)
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
    returnPeriod=int(Settings.objects.get(setID=2201).value)
    returnDate=timedelta(days=returnPeriod)+timezone.now()
    returnDate.replace(hour=23,minute=59,second=59,microsecond=999999)
    userAddData['returnDate']=returnDate
    serialized=UserSerializerStore(data=userAddData)
    bkNo=userAddData['bookNo']
    try:
        user=User.objects.get(bookNo=bkNo,returnStatus=False,regNo=userAddData['regNo'])
        return Response({"Detail":"Book issued already"})
    except User.DoesNotExist:
        try:
            book=Book.objects.get(serial=bkNo)
        except Book.DoesNotExist:
            return Response({"Detail":"Book not found.."},status=404)
        if serialized.is_valid():
            serialized.save()
            book.no_of_times_borrowed=F('no_of_times_borrowed')+1
            book.save()
        return redirect("user-list")

@api_view(['PUT'])
def userUpdate(request,reg,ser):
    userData=request.data
    user=get_object_or_404(klass=User,regNo=reg,bookNo=ser,
                        returnStatus=False)
    serialized=UserSerializerStore(instance=user,data=userData)
    if serialized.is_valid():
        serialized.save()
    return Response({"Detail":"Updated successfuly.."})
    
@api_view(['POST'])
def userReturn(request,reg,ser,status):
    user= get_object_or_404(klass=User,bookNo=ser,regNo=reg,returnStatus=False)
    if status==True:
        user.returnStatus=status
        user.save()
        return Response({"Detail":"Book returned successfully.."})
    elif status==False:
        returnPeriod=int(Settings.objects.get(setID=2201).value)
        returnDate=timedelta(days=returnPeriod)+timezone.now()
        returnDate.replace(hour=23,minute=59,second=59,microsecond=999999)
        user.returnDate=returnDate
        user.save()
        return Response({"Detail":"Book renewed successfully"})


@api_view(['DELETE'])
def userDelete(request,reg,ser):
    book=User.objects.filter(regNo=reg,bookNo=ser)
    if book.exists():
        book.delete()
        return redirect("user-list")
    else:
        return Response({"Detail":"user not found!!"})


@api_view(['PUT'])
def settingsParameters(request,code,val):
    sett=get_object_or_404(klass=Settings,setID=code)
    sett.value=val
    sett.save()
    return Response({"Detail":"Settings value changed successfully"})
