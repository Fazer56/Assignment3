from django.shortcuts import render
#import geo
import requests
import os

# Create your views here.
class appView:

    
    def volunteer(request):
        return render(request, 'volunteer/basic.html' , {'content':['Volunteering', 'Here is a map of all the places we will be volunteering']})
        

    def maploc(request):
        

        
        
        return render(request, 'volunteer/maps.html')

   # def location(request):

    
    def detail(request, member_id):
        return HttpResponse("<h2>Details for Album id" + str(member_id) + "</h2>"  )
        



    
#response = request.get(url) #this is used for 'get requests'
#response = request.post(url)

#API key = AIzaSyCrrN9Svur1OHJzFAOosSjh8k_mHWP86Hc
