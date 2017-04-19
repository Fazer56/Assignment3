
from django import forms

class Member(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=50)
    surname =  forms.CharField(label='Surname', max_length=50)
    address = forms.CharField(label='Address', max_length=150, blank = True)
    email = forms.EmailField(label='Email', max_length=100)
    
    #def __str__(self):
     #   return self.first_name + ' - ' + self.surname

