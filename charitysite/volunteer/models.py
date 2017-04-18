
from django.db import models

class Member(models.Model):
    first_name = models.CharField(max_length=50)
    surname =  models.CharField(max_length=50)
    address = models.CharField(max_length =150, blank=True)
    email = models.EmailField(max_length=100)
    
    def __str__(self):
        return self.first_name + ' - ' + self.surname

class Location(models.Model):
    building_name = models.CharField(max_length=50, blank = True)
    street_address= models.CharField(max_length=50)
    locality =models.CharField(max_length=50, blank = True)
    city= models.CharField(max_length=50)
    county =models.CharField(max_length=50)
    latitude = models.FloatField(max_length=30, blank = True)
    longitude = models.FloatField(max_length=30, blank = True)
    
    def __str__(self):
        return self.street_address + ', ' + self.city + ', ' + self.county 
    
    
