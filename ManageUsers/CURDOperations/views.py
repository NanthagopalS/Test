from django.http import JsonResponse
from django.shortcuts import render
from .models import UserDetails, AddressDetails
from .serializers import UserSerializer, UserAddressSerializer
import json
from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(http_method_names=["POST"])
def CreateUser(request):
    try:
        # data = json.loads(request.body)
        # # user = UserDetails(**data)
        # # user.save()
        # userdata = {"name":data.pop("name"),
        #             "dob":data.pop("dob"),
        #             "email":data.pop("email"),
        #             "mobile_number":data.pop("mobile_number")
        #             }
        # user = UserDetails.objects.create(**userdata)
        # address = AddressDetails.objects.create(user_id=user.id,**data)
        # # user.address_details_set.create(**data)
        # return JsonResponse({"Data": model_to_dict(user), "Message":"User Create Sucessfully", "StatusCode":200})
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data":serializer.data},status=status.HTTP_200_OK)
    except Exception as ex: 
        return JsonResponse({"Message": str(ex), "StatusCode":500})

def UpdateUser(request, id):
    try:
        data = json.loads(request.body)
        validate_data = {x:y for x,y in data.items() if y != ""}
        user = UserDetails.objects.filter(id = id).update(**validate_data)
        return JsonResponse("Update User",safe=False)
    except Exception as ex:
        return JsonResponse({"Message": str(ex), "StatusCode":500})

def GetAllUser(request):
    users = UserDetails.objects.all()
    data = [model_to_dict(x) for x in users]
    return JsonResponse({"Data": data })

def DeleteUser(request, id):
    try:
        user = UserDetails.objects.filter(id = id)
        name = user[0].name
        user.delete()
        return JsonResponse(f"{name} User Deleted Successfully",safe=False)
    except Exception as ex:
        return JsonResponse({"Message": str(ex), "StatusCode":500})
    
def GetUser(request, id):
    try:
        user = UserDetails.objects.filter(id = id)
        return JsonResponse({"Data": model_to_dict(user[0])})
    except Exception as ex:
        return JsonResponse({"Message": str(ex), "StatusCode":500})