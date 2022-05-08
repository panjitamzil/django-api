from django.db import models

# Create your models here.


class Payments(models.Model):
    Id = models.AutoField(primary_key=True)
    PaymentNumber = models.CharField(max_length=500)
    DueAmount = models.IntegerField()

class Users(models.Model):
    Id = models.AutoField(primary_key=True)
    Email = models.CharField(max_length=500)
    IsActive = models.BooleanField()
    Pay = models.ForeignKey(Payments, on_delete=models.CASCADE)

