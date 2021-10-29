import datetime

from django.core import serializers
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import HttpResponse
from itertools import chain

from django.db import models

from functools import reduce
from queryset_sequence import QuerySetSequence
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token


from myapp.models import advisor,user,bookingreq
from myapp.serializers import advisorSerializer,userSerializer,bookingreqSerializer
from rest_framework.decorators import api_view


@api_view(['POST','GET'])
def advisor_list(request):
    if request.method =="GET":
        data=list(advisor.objects.values())

        return JsonResponse(data,safe=False)
    if request.method=="POST":
        advisorlist_data=JSONParser().parse(request)
        advisorlist_data_serialized=advisorSerializer(data=advisorlist_data)
        if advisorlist_data_serialized.is_valid():
            advisorlist_data_serialized.save()
            return JsonResponse(advisorlist_data_serialized.data, status=status.HTTP_201_CREATED)
        return JsonResponse(advisorlist_data_serialized.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST','GET'])
def user_register(request):
    if request.method =="GET":
        data=list(user.objects.values())
        return JsonResponse(data,safe=False)

    if request.method == "POST":
        user_data=JSONParser().parse(request)
        user_data_serialized=userSerializer(data=user_data)

        if user_data_serialized.is_valid():
            user_data_serialized.save()
            data={}
            data['User_id']=user_data_serialized.data['id']

            return JsonResponse(data,status=status.HTTP_201_CREATED)
        return JsonResponse(user_data_serialized.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def user_login(request):
        if request.method == 'POST':
            user_data=JSONParser().parse(request)
            if 'email' not in user_data or 'password' not in user_data:
                return HttpResponse('fields are missing', status=status.HTTP_400_BAD_REQUEST)

            input_password=user_data['password']
            input_email=user_data['email']


            registered_user = user.objects.get(email=input_email)
            if input_password == registered_user.password:
                registered_user.login=True
                registered_user.save()
                registered_user_serialized = userSerializer(registered_user)
                token= jwt.encode({'email': input_email, 'password': input_password}, 'MySecretKey', algorithm='HS256')


                return JsonResponse(registered_user_serialized.data,safe=True, status=status.HTTP_200_OK)


            else:
                return HttpResponse("email/password combination is wrong",status=status.HTTP_401_UNAUTHORIZED)
            #     # return JsonResponse("email/password combination was wrong", status=status.HTTP_401_UNAUTHORIZED )


@api_view(['GET'])
def useradvisor_list(request,user_id):
    if request.method =='GET':
        loggedinuser=user.objects.get(id=user_id)
        if loggedinuser.login:
            person = list(advisor.objects.values("name", "photourl", "id"))
            return JsonResponse(person,safe=False,status=status.HTTP_200_OK)
        else:
            return HttpResponse('user not logged in',status=status.HTTP_400_BAD_REQUEST)





@api_view(['POST'])
def bookingtime(request,user_id,advisor_id):
    if request.method =='POST':
        loggedinuser = user.objects.get(id=user_id)
        if loggedinuser.login:
            l= JSONParser().parse(request)
            bookingtimedata={}
            bookingtimedata['user_id']=user_id
            bookingtimedata['advisor_id']=advisor_id
            givenadvisor=advisor.objects.get(id=advisor_id)
            bookingtimedata_serialized = bookingreqSerializer(data=bookingtimedata)
            if bookingtimedata_serialized.is_valid():
                bookingtimedata_serialized.save()
                givenadvisor.bookingtime = l['bookingtime']
                givenadvisor.booking_id = bookingtimedata_serialized.data['id']
                givenadvisor.save()
                return HttpResponse('booked', status=status.HTTP_201_CREATED)

            return JsonResponse(bookingtimedata_serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        return HttpResponse('user not logged in', status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getallbookedadivsorlist(request,user_id):
    if request.method=='GET':
        loggedinuser = user.objects.get(id=user_id)
        if loggedinuser.login:
            bookingtimedata=bookingreq.objects.filter(user_id=user_id)
            # return JsonResponse(bookingtimedata,safe=False,status=status.HTTP_200_OK)
            res=[]
            for k in bookingtimedata:
                res+=list(advisor.objects.filter(id=k.advisor_id).values())

            return JsonResponse(res,safe=False,status=status.HTTP_200_OK)
        return HttpResponse('user not logged in', status=status.HTTP_400_BAD_REQUEST)








