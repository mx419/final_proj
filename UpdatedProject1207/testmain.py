import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import operator
import sys
import re 
from user_defined_exceptions import *
import mapplot #plot map
import warnings
import visualizationTool as vs
import general_functions as gf
import freq_station as fs


print 'Initilizing...'
print "Reading the data..."
data = pd.read_csv('Citibike_final.csv')

year = 2014
month = 1
top_choice = 5

data_month = gf.data_extract(data, year, month, year, month)


loc_data = fs.station_info(data_month, year, month)
fs.high_freq_station(data_month, top_choice)
# map_plot_obj = mapplot.MapPlot(loc_data,1)