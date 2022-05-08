from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from UserApp.models import Users, Payments

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=('Id', 'Email', 'IsActive', 'Pay')

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payments
        fields=('Id', 'PaymentNumber', 'DueAmount')