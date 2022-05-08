from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from UserApp.models import Users, Payments
from UserApp.serializers import UserSerializer, PaymentSerializer
# Create your views here.

@csrf_exempt
def userAPI(request, id=0):
    if request.method == 'GET':
        if id != 0:
            user = Users.objects.get(Id = id)
            users_serializer = UserSerializer(user, many=False)
            return JsonResponse(users_serializer.data, safe=False)
        else:
            users = Users.objects.all()
            users_serializer = UserSerializer(users, many=True)
            return JsonResponse(users_serializer.data, safe=False)
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        users_serializer = UserSerializer(data=user_data)
        print(users_serializer)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Data was inserted", safe=False)
        return JsonResponse("Failed to insert data", safe=False)
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user = Users.objects.get(Id = user_data['Id'])
        users_serializer = UserSerializer(user,data=user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Data was updated", safe=False)
        return JsonResponse("Failed to update data", safe=False)
    elif request.method == 'DELETE':
        user = Users.objects.get(Id = id)
        user.delete()
        return JsonResponse("Data was deleted", safe=False)

@csrf_exempt
def paymentAPI(request, id=0):
    if request.method == 'GET':
        if id != 0:
            user = Payments.objects.get(Id = id)
            payments_serializer = PaymentSerializer(user, many=False)
            return JsonResponse(payments_serializer.data, safe=False)
        else:
            users = Payments.objects.all()
            payments_serializer = PaymentSerializer(users, many=True)
            return JsonResponse(payments_serializer.data, safe=False)
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        payments_serializer = PaymentSerializer(data=user_data)
        if payments_serializer.is_valid():
            payments_serializer.save()
            return JsonResponse("Data was inserted", safe=False)
        return JsonResponse("Failed to insert data", safe=False)
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user = Payments.objects.get(Id = user_data['Id'])
        payments_serializer = PaymentSerializer(user,data=user_data)
        if payments_serializer.is_valid():
            payments_serializer.save()
            return JsonResponse("Data was updated", safe=False)
        return JsonResponse("Failed to update data", safe=False)
    elif request.method == 'DELETE':
        user = Payments.objects.get(Id = id)
        user.delete()
        return JsonResponse("Data was deleted", safe=False)
