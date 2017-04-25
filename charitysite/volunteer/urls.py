#local urls.py file
from django.conf.urls import url, include
from . import views



urlpatterns = [

    

    #url(r'^', views.appView.postLocation, name = 'postLocation'),

    url(r'^', views.appView.member, name = 'member'),

    
    
    #url(r'^(?P<member_id>[0-9]+)/$', views.appView.detail, name = 'detail'),

    #url(r'^(?P<>))
]
