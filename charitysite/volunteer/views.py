from django.shortcuts import render
from django.http import HttpResponse
from volunteer.forms import MemberForm
from volunteer.models import Member 
from volunteer.geo import GeoLoc
from django.http import HttpResponseRedirect

import requests
import os


# Create your views here.
class appView:
            
    
    def member(request):

        
        lat = 53.3372027
        lon = -6.2673709
        geo = GeoLoc(lat, lon)

        
        lat1 = 53.345192
        lon1 = -6.255031
        geo1 = GeoLoc(lat1, lon1)

        
        lat2 = 53.339071
        lon2 = -6.260061
        geo2 = GeoLoc(lat2, lon2)

        lat3 = 53.347185
        lon3 = -6.259243
        geo3 = GeoLoc(lat3, lon3)

        lat4 = 53.343498
        lon4 = -6.242177
        geo4 = GeoLoc(lat4, lon4)

        lat5 = 53.381514
        lon5 = -6.073211
        geo5 = GeoLoc(lat5, lon5)

        

        results = geo.findLoc(geo.lat, geo.lon)
        results1 = geo1.findLoc(geo1.lat, geo1.lon)
        results2 = geo2.findLoc(geo2.lat, geo2.lon)
        results3 = geo3.findLoc(geo3.lat, geo3.lon)
        results4 = geo4.findLoc(geo4.lat, geo4.lon)
        results5 = geo5.findLoc(geo5.lat, geo5.lon)

        locations = [results, results1, results2, results3, results4, results5]
        
        if request.method == 'POST': #If form has been submitted
            form = MemberForm(request.POST) # A form bound to the POST data
            
            if form.is_valid():# check the form has all the valid fields
                first_name = request.POST.get('first_name', '')
                surname = request.POST.get('surname', '')
                email = request.POST.get('email', '')
                address = request.POST.get('address', '')
                
                member_obj = Member(first_name = first_name, surname = surname, email = email, address = address)
                member_obj.save() #the filled out fields in the form are stored into the database

                return render(request, 'volunteer/thanks.html', {'appreciation' : ['Thanks for signing up!']})

        else: 
            form = MemberForm()#error checking if form is incorrect

        context = { "lat" : lat,
            "lon" : lon, "lat1" : lat1, "lon1" : lon1, "lat2" : lat2, "lon2" : lon2, "lat3" : lat3,
            "lon3" : lon3, "lat4" : lat4, "lon4" : lon4, "lat5" : lat5, "lon5" : lon5,
            "form": form, "locations" : locations     }
        
        return render(request, 'volunteer/basic.html', context)





    
#response = request.get(url) #this is used for 'get requests'
#response = request.post(url)

#API key = AIzaSyCrrN9Svur1OHJzFAOosSjh8k_mHWP86Hc
