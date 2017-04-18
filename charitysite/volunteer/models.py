from django.db import models

class Member(models.Model):
    first_name = models.CharField(max_length=50)
    surname =  models.CharField(max_length=50)
    address = models.CharField(max_length =150, blank=True)
    email = models.EmailField(max_length=100)
    
    def __str__(self):
        return self.first_name + ' - ' + self.surname
