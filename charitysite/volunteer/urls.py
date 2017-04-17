#local urls.py file
from django.conf.urls import url, include
from . import views



urlpatterns = [
   # url(r'^volunteer', views.appView.maploc, name='maploc'),
    url(r'', views.appView.volunteer, name='volunteer'),
    
    #url(r'^$', views.appView.index, name='index'),#return file 'views' function'index'
   
    

]
