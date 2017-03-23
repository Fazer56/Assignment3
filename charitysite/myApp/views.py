from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'myApp/home.html') #return render  looks in a templates directory 


