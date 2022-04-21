from django.db import models


# Create your models here.
class Customer(models.Model):
    client_name = models.CharField(max_length=30) 
    gst_number = models.CharField(max_length=30) 
    client_id = models.CharField(max_length=30) 
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=30)
    address = models.CharField(max_length=30)