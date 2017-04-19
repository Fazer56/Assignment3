#local urls.py file
from django.conf.urls import url, include
from . import views



urlpatterns = [
    #/volunteer/
    url(r'^volunteer/$', views.appView.volunteer, name='volunteer'),

    url(r'^volunteer/$', views.appView.member, name = 'member'),
    #/volunteer/700/
    #url(r'^(?P<member_id>[0-9]+)/$', views.appView.detail, name = 'detail'),

    #url(r'^(?P<>))
]
