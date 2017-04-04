from django.shortcuts import render
import requests

# Create your views here.
class appView:
    
    def volunteer(request):
        return render(request, 'volunteer/basic.html' , {'content':['Volunteering', 'Here is a map of all the places we will be volunteering']})


#API key = AIzaSyCrrN9Svur1OHJzFAOosSjh8k_mHWP86Hc
