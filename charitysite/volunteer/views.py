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

        geo = GeoLoc(53.3372027, -6.2673709)
        lat = 53.3372027
        lon = -6.2673709

        results = geo.findLoc(geo.lat, geo.lon)
        
        if request.method == 'POST': #If form has been submitted
            form = MemberForm(request.POST) # A form bound to the POST data
            
            if form.is_valid():# check the form has all the valid fields
                first_name = request.POST.get('first_name', '')
                surname = request.POST.get('surname', '')
                email = request.POST.get('email', '')
                address = request.POST.get('address', '')
                
                member_obj = Member(first_name = first_name, surname = surname, email = email, address = address)
                member_obj.save() #the filled out fields in the form are stored into the database

                return HttpResponseRedirect('volunteer/basic.html')

        else: 
            form = MemberForm()#error checking if form is incorrect

        context = { "lat" : lat,
        "lon" : lon, "form": form, "results" : results }
        
        return render(request, 'volunteer/basic.html', context)





    
#response = request.get(url) #this is used for 'get requests'
#response = request.post(url)

#API key = AIzaSyCrrN9Svur1OHJzFAOosSjh8k_mHWP86Hc
