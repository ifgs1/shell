from django.db import models
from django.contrib.auth.models import User


# Create your models here.

Design_Status = ((1,'IN_PROGRESS'), (2,'AVAILABLE'))


class Usuario(models.Model):
    full_name = models.CharField(max_length=100,blank=True)
    user_identifiation = models.BigIntegerField
    birth_date = models.CharField(max_length=100,blank=True)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    user = models.OneToOneField(User,null=True)

class Trayecto(models.Model):
     name = models.CharField(max_length=50, blank=True)
     price = models.CharField(max_length=50, blank=True)
     description = models.CharField(max_length=250, blank=True)
     latitudeOR = models.CharField(max_length=250, blank=True)
     longitudeOR = models.CharField(max_length=250, blank=True)
     latitudeDE = models.CharField(max_length=250, blank=True)
     longitudeDE = models.CharField(max_length=250, blank=True)
     date_ride = models.CharField(max_length=100, blank=True)
     seats = models.BigIntegerField(blank=False, null=False)
     plates = models.CharField(max_length=50, blank=True)
     usuario = models.ForeignKey(Usuario, null=True)