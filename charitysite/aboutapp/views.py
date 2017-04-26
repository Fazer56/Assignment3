from django.shortcuts import render

# Create your views here.
class appView:
    
    def about(request):
        
        return render(request, 'aboutapp/basic.html') #return render  looks in a templates directory 

