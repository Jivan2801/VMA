from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):
    Vehicle_no = models.CharField(max_length=8)
    Vehicle_type = models.CharField(max_length=20)
    Vehicle_model = models.CharField(max_length=30)
    Vehicle_des = models.TextField()


class user(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True , blank=True )
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=25)
    role = models.CharField(max_length=25)