from __future__ import division
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import operator
from matplotlib.gridspec import GridSpec


# DS-GA 1007 Final Project
# Visualization tool
# Author: Sida Ye

"""
Provide data visualization for citibike data in certain period by user's requirement

"""

class visualizationTool(object):
    def __init__(self, data, year, month):
        self.data = data
        self.year = year
        self.month = month


    def pieplot(self, variable):
        """ Plot pie plot for gender or usertype in certain period """
        variable_type = self.data[variable].unique()
        variable_size = []
        if variable == 'gender':
            for i in np.sort(variable_type):
                variable_size.append(round((sum(self.data[variable] == i) / self.data.shape[0] * 100), 2))    # calculate distirbution
            # Gender (Zero=unknown; 1=male; 2=female)
            labels = 'Unknown', 'Male', 'Female'
            sizes = variable_size
            colors = ['lightyellow','lightskyblue', 'lightcoral']
            explode = (0, 0.1, 0.1)  # "explode" the distribution of male and female

            plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                    autopct='%1.1f%%', shadow=True, startangle=90)
            # Set aspect ratio to be equal so that pie is drawn as a circle.
            plt.axis('equal')
            plt.title('Gender Distribution in {}-{}'.format(self.year, self.month), fontsize = 12,y = 1,x=0.12,bbox={'facecolor':'0.8', 'pad':5})
            plt.show()

        elif variable == 'usertype':
            # usertype (Zero=Customer, 1=Subscriber)
            for i in range(2): # change to 0, 1
                variable_size.append(round((sum(self.data[variable] == i) / self.data.shape[0] * 100), 2))    # calculate distribution
            labels = 'Subscriber', 'Customer'
            sizes = variable_size
            colors = ['lightcoral','lightskyblue']
            explode = (0, 0.1)  # only "explode" the subscriber

            plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                    autopct='%1.1f%%', shadow=True, startangle=90)
            # Set aspect ratio to be equal so that pie is drawn as a circle.
            plt.axis('equal')
            plt.title('User Type Distribution in {}-{}'.format(self.year, self.month), fontsize = 12,y = 1,x=0.12,bbox={'facecolor':'0.8', 'pad':5})
            plt.show()
    


    def plot_daily_freq(self, show_mile=False):
        """ Plot bar plot for the daily usage or miles in certain month """
        if show_mile == False:
            self.data['startdate'] = [self.data['starttime'][i].split(' ')[0] for i in range(self.data.shape[0])]
            freq_date = Counter(self.data['startdate'])
            sorted_freq_date = sorted(freq_date.items(), key=operator.itemgetter(0))
            df = pd.DataFrame(sorted_freq_date, columns=['Date', 'freq'])
            df = df.set_index('Date')
            df.plot(kind='bar',legend=False, color='lightblue',alpha=0.8,figsize=(13,9))
            plt.ylabel('Usage', fontsize=16)
            plt.xticks(np.arange(len(sorted_freq_date))-1, rotation=45)
            plt.grid(True)
            plt.title('Daily trips for {}'.format(str(self.year)+'-'+str(self.month).zfill(2)))
            plt.show()
        elif show_mile == True:
            self.data['startdate'] = [self.data['starttime'][i].split(' ')[0] for i in range(self.data.shape[0])]
            trip_usage = {}
            for i in self.data['startdate'].unique():
                trip_usage[i] = round(sum(self.data[self.data['startdate'] == i]['tripduration']) * 3.33 / 1000, 2)   # bike speed 3.33m/s          
            df = pd.Series(trip_usage)
            df = pd.DataFrame(df, columns=['miles'])
            df.plot(kind='bar',legend=False, color='lightblue',alpha=0.8,figsize=(13,9))
            plt.ylabel('Miles', fontsize=16)
            plt.xticks(np.arange(len(sorted_freq_date))-1, rotation=45)
            plt.grid(True)
            plt.title('Miles Traveled Daily for {}'.format(str(self.year)+'-'+str(self.month).zfill(2)))
            plt.show()
        else:   # how to handel exception
            raise KeyError('Wrong input format for show_mile')






