import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import operator
from collections import Counter

# DS-GA 1007 Final Project
# Station frequency Calculation
# Author: Sida Ye

# need to modify data import 
"""Function to generate Station id as key, location and station name as value"""
def station_info(year, month, stat_type):
    data = pd.read_csv('{}-{} - Citi Bike trip data.csv'.format(year, month))
    freqs = Counter(data['start station id'])
    location_dict = {}
    for id in data['{} station id'.format(stat_type)].unique():
        if id not in location_dict.keys():
            location_dict[id] = data[data['start station id'] == id][['start station latitude', 'start station longitude','start station name']].iloc[0].values
            location_dict[id] = np.append(location_dict[id], freqs[id])
    return location_dict
    

"""This function takes input as year, month, stat_type('start' or 'end'), top_k(number of top k station you want to know)
    It will return a list of highest frequency station name."""

def high_freq_station(year, month, stat_type, top_k):
    data = pd.read_csv('{}-{} - Citi Bike trip data.csv'.format(year, month)) # import data
    freqs = Counter(data['{} station id'.format(stat_type)]) # count freq for each unique station
    sorted_freqs = sorted(freqs.items(), key=operator.itemgetter(1), reverse=True) # sort by freq
    topk_stations = [i[0] for i in sorted_freqs[:top_k]] # show topk station id
    loc_dict = station_info(year, month, stat_type)
    topk_stations_name = []
    for id in topk_stations:
        topk_stations_name.append(loc_dict[id][2])
    return topk_stations_name
    
    