import sys
import os
from pygeocoder import Geocoder

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class GeoLoc:
    def __init__(self, lat, lon):
        #super(GeoLoc, self).__init__()
        self.lat = lat
        self.lon = lon
    
    
    def reading(self):
        self.lon = []
        self.lat = []
        self.loc ={}

        
        w2 =""
        with open('templates/volunteer/includes/maps.html', 'r') as file:
            for line in file:
                if 'lat:' in line:
                    word = line.split(',')[0]
                    w2 = line.split('lng:')[1]
                                            
                    self.lon.append(float(w2.split('}')[0]))

                    self.lat.append(float(word.split(':')[1]))
                                            

                                            
                    print(word)
                    print(w2)
                                            

        self.results = Geocoder.reverse_geocode(self.lat[0], self.lon[0])
        print(self.results.city)

    def findLoc(self, lat, lon):
        self.lat = lat
        self.lon = lon

        self.results = Geocoder.reverse_geocode(self.lat, self.lon)

        print(self.results)
            
        return self.results

    

            
def main():
    
    geo = GeoLoc(53.3372027, -6.2673709)

    print(geo.lat)
    print(geo.lon)
    
    geo.findLoc(geo.lat, geo.lon)
    
    

    

if __name__ == '__main__':
    main() 

