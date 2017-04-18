import sys
import os
from pygeocoder import Geocoder

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class GeoLoc(QWidget):

    
    def __init__(self):
        super(GeoLoc, self).__init__()
        self.initUI()

    def initUI(self):
        self.win = QWidget()
        self.win.resize(1500, 900)
        self.reading()
    
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

        
        
        self.loc = dict(zip(self.lat, self.lon))

        print(self.loc)
                
            


    

            
def main():
    
    app = QApplication(sys.argv)
    appform=GeoLoc()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main() 

