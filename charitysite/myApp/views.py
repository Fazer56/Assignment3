from django.shortcuts import render

# Create your views here.
class appView:
    
    def index(request):

        items = ["Toothbrush", "Toothpaste", "Deodorant", "Sponge", "Face Cloth", "Wet Wipes", "Soap", "Hand Cream"]
        items2 = ["Tissues", "Ziploc Bags", "Hats", "Socks", "Gloves", "Plasters", "Sanitary Towels", "Cotton Buds"]
        items3 = ["Nail File", "Water", "Cereal Bar", "Sweat Treat", "Toilet Roll", "Comb or Brush", "Lip Balm"]

        info = "All the info on volunteering can be found on the volunteer page. Just click the map image to be brought there!"
        
        context = { "items" : items,
                    "items2" : items2,
                    "items3" : items3,
                     "info" : info      }
        
        return render(request, 'myApp/home.html', context) #return render  looks in a templates directory 


    def contact(request):
        return render(request, 'myApp/basic.html', {'content':['If you would like to get involved, please email us', 'dignitypacks@mail.ie'] }) #adding an about request for about page calling it basic because it's a basic html page that can be used again

    

