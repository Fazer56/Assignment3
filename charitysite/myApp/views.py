from django.shortcuts import render

# Create your views here.
class appView:
    
    def index(request):
        return render(request, 'myApp/home.html') #return render  looks in a templates directory 


    def contact(request):
        return render(request, 'myApp/basic.html', {'content':['If you would like to get involved, please email us', 'dignitypacks@mail.ie'] }) #adding an about request for about page calling it basic because it's a basic html page that can be used again

