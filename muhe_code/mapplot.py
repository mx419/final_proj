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
    #def __init__(self,longs,lats,freqs):
    def __init__(self,dots,month):
        self.dots = dots
        longs = dots['long']
        longs = longs.tolist()
        self.longs = [float(x) for x in longs]
        lats = dots['lat']
        lats = lats.tolist()
        self.lats = [float(x) for x in lats]
        self.freqs = dots['freq']
        self.v_max = self.freqs.max()
        self.v_min = self.freqs.min()
        self.v_median = self.freqs.median()
        self.freqs_list = self.freqs.tolist()
        self.month = str(month)

        

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
        plt.figure(figsize=(20,10))
        plt.title('frequency distribution of citi bike stations in 2014.'+self.month) 
        map = Basemap(projection='merc', resolution = 'i',  area_thresh = 0.1,llcrnrlon=-74.04, llcrnrlat= 40.68,urcrnrlon= -73.937599, urcrnrlat=40.7705)
        map.drawcoastlines(color = 'r')
        map.drawcountries(color = 'aqua')
        map.drawmapboundary(zorder=0)

        x2,y2 = map(self.longs,self.lats)
        for i in range(len(x2)):
            map.plot(x2[i], y2[i], marker = 'o',color = self.get_color_tuple(self.freqs_list[i]),markersize=16,zorder = 1)
        # 2 points as legend
        legend_high_x,legend_high_y = map(-74.036,40.7685)
        legend_low_x,legend_low_y = map(-74.036,40.763)
        map.plot(legend_high_x,legend_high_y,marker = 'o',color = (1,0,0),markersize=20,zorder = 1)
        map.plot(legend_low_x,legend_low_y,marker = 'o',color = (0,0,1),markersize=20,zorder = 1)
        plt.text(legend_high_x+300, legend_high_y-100, 'High Freq',fontsize=12)
        plt.text(legend_low_x+300, legend_low_y-100, 'Low Freq',fontsize=12)
        plt.show()

    def draw_top_k_freq_map(self,k):
        top_k_index = self.dots.sort('freq',ascending=False)[:k].index
        plt.figure(figsize=(20,10))
        plt.title('Top '+str(k)+' frequency citi bike stations in 2014.'+self.month) 
        map = Basemap(projection='merc', resolution = 'i',  area_thresh = 0.1,llcrnrlon=-74.04, llcrnrlat= 40.68,urcrnrlon= -73.937599, urcrnrlat=40.7705)
        map.drawcoastlines(color = 'r')
        map.drawcountries(color = 'aqua')
        map.drawmapboundary(zorder=0)

        x2,y2 = map(self.longs,self.lats)
        for i in top_k_index:
            map.plot(x2[i], y2[i], marker = 'o',color = self.get_color_tuple(self.freqs_list[i]),markersize=14,zorder = 1)
            plt.text(x2[i]+200, y2[i], self.dots.ix[i]['name'],fontsize = 7)
        # 2 points as legend
        legend_high_x,legend_high_y = map(-74.036,40.7685)
        legend_low_x,legend_low_y = map(-74.036,40.763)
        map.plot(legend_high_x,legend_high_y,marker = 'o',color = (1,0,0),markersize=20,zorder = 1)
        map.plot(legend_low_x,legend_low_y,marker = 'o',color = (0,0,1),markersize=20,zorder = 1)
        plt.text(legend_high_x+300, legend_high_y-100, 'High Freq',fontsize=12)
        plt.text(legend_low_x+300, legend_low_y-100, 'Low Freq',fontsize=12)
        plt.show()
        

    



