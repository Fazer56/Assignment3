#local urls.py file
from django.conf.urls import url, include
from . import views



urlpatterns = [
    url(r'^aboutapp/', views.appView.about, name='about'), 
]
