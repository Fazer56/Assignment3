from .models import Member
from django import forms

class MemberForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=50, required = True)
    surname =  forms.CharField(label='Surname', max_length=50, required = True)
    email = forms.EmailField(label='Email', max_length=100, required = True)
    address = forms.CharField(label='Address', max_length=150, required = False)
