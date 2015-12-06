'''This module contains a class to plot frequency results on the basemap'''

import pandas as pd
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

#author: Muhe Xie
#netID: mx419
#date: 12/05/2015

#to be done next: 
#1 show most used station points station name text and locations
#2 heat map

class MapPlot(object):
    '''this class contains methods to visualize the station location data and frequency data on the map
    '''
    def __init__(self,longs,lats,freqs):
        self.longs = longs
        self.lats = lats
        self.freqs = freqs
        self.v_max = freqs.max()
        self.v_min = freqs.min()
        self.v_median = freqs.median()
        self.freqs_list = self.freqs.tolist()
        pass

    def get_red_color(self,maxvalue,minimunvalue,this_value):
        #get the red distribution in the rgb color
        ranger = maxvalue - minimunvalue
        return 1.0 - float((this_value-minimunvalue))/float(ranger)

    def get_blue_color(self,maxvalue,minimunvalue,this_value):
        #get the blue distribution in the rgb color
        ranger = maxvalue - minimunvalue
        return 1.0 - float((this_value-minimunvalue))/float(ranger)

    def get_color_tuple(self,freq):
        #get the rgb color tuple
        if freq>=self.v_median:
            a = self.get_red_color(self.v_max,self.v_median,freq)
            return (1,a,a)
        else:
            a = self.get_blue_color(self.v_median,self.v_min,freq)
            return (a,a,1)

    def draw_freq_map(self):
        map = Basemap(projection='merc', resolution = 'i',  area_thresh = 0.1,llcrnrlon=-74.04, llcrnrlat= 40.68,urcrnrlon= -73.937599, urcrnrlat=40.7705)
        map.drawcoastlines(color = 'r')
        map.drawcountries(color = 'aqua')
        map.drawmapboundary(zorder=0)

        x2,y2 = map(self.longs,self.lats)
        for i in range(len(x2)):
            map.plot(x2[i], y2[i], marker = 'o',color = self.get_color_tuple(self.freqs_list[i]),markersize=10,zorder = 1)

        plt.show()

    



