import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mapplot
import mapplot
import warnings

#this only used for try by my self

dots = pd.read_csv('loc_freq.csv')
dots=dots.drop(301)
freqs = dots['freq'].tolist()
#get longitudes
longs = dots['long']
longs = longs.tolist()
longs = [float(x) for x in longs]
#get latitudes
lats = dots['lat']
lats = lats.tolist()
lats = [float(x) for x in lats]

v_max = dots['freq'].max()
v_min = dots['freq'].min()
v_median = dots['freq'].median()

dots22 = pd.read_csv('1007 data/freq_201408.csv')

#obj = mapplot.MapPlot(longs,lats,dots['freq'])
obj = mapplot.MapPlot(dots22,3)

while True:
    a = raw_input('?')
    if a == '1':
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            obj.draw_freq_map()
            obj.draw_top_k_freq_map(3)
            obj.draw_heat_map()
    else:
       break