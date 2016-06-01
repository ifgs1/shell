from django.db import models
from django.contrib.auth.models import User
from enum import Enum


# Create your models here.

Design_Status = ((1,'IN_PROGRESS'), (2,'AVAILABLE'))


class Administrator(models.Model):
    company = models.CharField(max_length=100,blank=True)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    user = models.OneToOneField(User,null=True)
    url = models.CharField(max_length=100,blank=True)

class Proyecto(models.Model):
    name = models.CharField(max_length=50,blank=True)
    description = models.CharField(max_length=250,blank=True)
    image = models.CharField(max_length=500,blank=True)
    estimated_price = models.BigIntegerField
    administrador = models.ForeignKey(User,null=True)

class Designer(models.Model):
    name = models.CharField(max_length=50,blank=True)
    lastname = models.CharField(max_length=50,blank=True)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    def natural_key(self):
        object = {
            'email':self.email,
            'name':self.name,
            'lastname':self.lastname
        }
        return object

class Design(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=Design_Status)
    price = models.BigIntegerField(blank=False, null=False)
    imageFile = models.ImageField(upload_to='images',null=True)
    designer = models.ForeignKey(Designer,null=True)
    project = models.ForeignKey(Proyecto,null=True)