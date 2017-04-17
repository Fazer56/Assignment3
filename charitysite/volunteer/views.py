from django.shortcuts import render
import requests

# Create your views here.
class appView:

    
    def volunteer(request):
        return render(request, 'volunteer/basic.html' , {'content':['Volunteering', 'Here is a map of all the places we will be volunteering']})

    def maploc(request):
        return render(request, 'volunteer/maps.html')
    
#response = request.get(url) #this is used for 'get requests'
#response = request.post(url)

#API key = AIzaSyCrrN9Svur1OHJzFAOosSjh8k_mHWP86Hc
