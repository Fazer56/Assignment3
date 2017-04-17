from django.shortcuts import render

# Create your views here.
class appView:
    
    def about(request):
        return render(request, 'About/basic.html', {'content': ['This is the about page for the site!']}) #return render  looks in a templates directory 

