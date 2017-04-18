from django.shortcuts import render
from pygeocoder import Geocoder
import requests
import os

# Create your views here.
class appView:

    
    
    def volunteer(request):
        dude = "sahahha"
        #return render(request, 'volunteer/basic.html' , {'content':['Volunteering', 'Here is a map of all the places we will be volunteering']})
        return render(request, 'volunteer/basic.html' , dude)
        return(dude)


    def maploc(request):
        return render(request, 'volunteer/maps.html')


    
                    



    
#response = request.get(url) #this is used for 'get requests'
#response = request.post(url)

#API key = AIzaSyCrrN9Svur1OHJzFAOosSjh8k_mHWP86Hc
