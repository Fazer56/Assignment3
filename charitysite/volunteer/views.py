from django.shortcuts import render
from volunteer.forms import MemberForm
from volunteer.models import Member
#import geo
import requests
import os



# Create your views here.
class appView:

    
    def volunteer(request):
        return render(request, 'volunteer/basic.html')
            
    def detail(request, member_id):
        return HttpResponse("<h2>Details for Album id" + str(member_id) + "</h2>"  )

    def member(request):
        if request.method == 'POST': #If form has been submitted

            form = MemberForm(request.POST) # A form bound to the POST data
            if form.is_valid():# check the form has all the valid fields
                

    
#response = request.get(url) #this is used for 'get requests'
#response = request.post(url)

#API key = AIzaSyCrrN9Svur1OHJzFAOosSjh8k_mHWP86Hc
