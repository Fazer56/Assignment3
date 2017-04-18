from django.db import models

class Volunteer(models.Model):
    first_name = models.CharField(max_length=50)
    surname =  models.CharField(max_length=50)
    address = models.CharField(max_length =150, blank=True)
    email = models.EmailField(max_length=100)
    
    
