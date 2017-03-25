#local urls.py file
from django.conf.urls import url, include
from . import views



urlpatterns = [
    url(r'^$', views.appView.index, name='index'),#return file 'views' function'index'
    url(r'^about/', views.appView.about, name='about'), 
]
