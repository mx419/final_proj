from __future__ import division
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import operator


# DS-GA 1007 Final Project
# Visualization tool
# Author: Sida Ye

"""
Provide data visualization for citibike data in certain period by user's requirement

"""

# class visulizationTool(object):
#     # def __init__(self, data, startyear, startmonth, endyear, endmonth, variable):
#     #     self.data = data


def pieplot(data, startyear, startmonth, endyear, endmonth, variable):
    """ Plot pie plot for gender or usertype in certain period """
    variable_type = data[variable].unique()
    variable_size = []
    if variable == 'gender':
        for i in np.sort(variable_type):
            variable_size.append(round((sum(data[variable] == i) / data.shape[0] * 100), 2))    # calculate distirbution
        # Gender (Zero=unknown; 1=male; 2=female)
        labels = 'Unknown', 'Male', 'Female'
        sizes = variable_size
        colors = ['lightyellow','lightskyblue', 'lightcoral']
        explode = (0, 0.1, 0.1)  # "explode" the distribution of male and female

        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=90)
        # Set aspect ratio to be equal so that pie is drawn as a circle.
        plt.axis('equal')
    elif variable == 'usertype':
        # usertype (Zero=Customer, 1=Subscriber)
        for i in ['Subscriber', 'Customer']:
            variable_size.append(round((sum(data[variable] == i) / data.shape[0] * 100), 2))    # calculate distribution
        labels = 'Subscriber', 'Customer'
        sizes = variable_size
        colors = ['lightcoral','lightskyblue']
        explode = (0, 0.1)  # only "explode" the subscriber

        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=90)
        # Set aspect ratio to be equal so that pie is drawn as a circle.
        plt.axis('equal')


def plot_daily_freq(data, year, month, stat_type, show_mile):
    """ Plot bar plot for the daily usage or miles in certain month """
    if show_mile == False:
        data['{}date'.format(stat_type)] = [data['{}time'.format(stat_type)][i].split(' ')[0] for i in range(data.shape[0])]
        freq_date = Counter(data['startdate'])
        sorted_freq_date = sorted(freq_date.items(), key=operator.itemgetter(0))
        df = pd.DataFrame(sorted_freq_date, columns=['Date', 'freq'])
        df = df.set_index('Date')
        plt.figure()
        df.plot(kind='bar',legend=False, color='lightblue',alpha=0.8,figsize=(15,10))
        plt.ylabel('Usage', fontsize=16)
        plt.grid(True)
        plt.title('Daily trips for {}'.format(str(year)+'-'+str(month).zfill(2)))
    elif show_mile == True:
        data['{}date'.format(stat_type)] = [data['{}time'.format(stat_type)][i].split(' ')[0] for i in range(data.shape[0])]
        trip_usage = {}
        for i in data['startdate'].unique():
            trip_usage[i] = round(sum(data[data['startdate'] == i]['tripduration']) * 3.33 / 1000, 2)           
        df = pd.Series(trip_usage)
        df = pd.DataFrame(df, columns=['miles'])
        df.plot(kind='bar',legend=False, color='lightblue',alpha=0.8,figsize=(15,10))
        plt.ylabel('Miles', fontsize=16)
        plt.grid(True)
        plt.title('Miles Traveled Daily for {}'.format(str(year)+'-'+str(month).zfill(2)))
    else:
        return 'Wrong input'

# need to modify data import for these two functions
def cumulative_usage_plot(endyear,endmonth):
    """ Show bar plot for cumulative usage from launch date to user-input date """
    usage_list = []
    for date in getfilenames(2013,7,endyear,endmonth):
        data = pd.read_csv('data/{} - Citi Bike trip data.csv'.format(date))
        usage_list.append(data.shape[0])
    df = pd.DataFrame(np.cumsum(usage_list), index = getfilenames(2013,7,endyear,endmonth))
    df.plot(kind='bar',legend=False, color='lightblue')
    plt.xlabel('Date')
    plt.ylabel('Number')
    plt.yticks(np.linspace(df[0][0], df[0][df.shape[0]-1],8))
    plt.grid(True)
    plt.title('Total trips between {} and {}'.format('2013-07', str(endyear)+'-'+str(endmonth).zfill(2)))


def cumulative_annual_plot(endyear, endmonth):
    """ Show bar plot for cumulative number of annual membership from launch date to user-input date """
    member_list = []
    for date in getfilenames(2013,7,endyear,endmonth):
        data = pd.read_csv('data/{} - Citi Bike trip data.csv'.format(date))
        member_list.append(sum(data['usertype']=='Subscriber'))
    df = pd.DataFrame(np.cumsum(member_list), index = getfilenames(2013,7,endyear,endmonth))
    df.plot(kind='bar',legend=False, color='lightblue')
    plt.xlabel('Date')
    plt.ylabel('Number')
    plt.yticks(np.linspace(df[0][0], df[0][df.shape[0]-1],8))
    plt.grid(True)
    plt.title('Total annual member between {} and {}'.format('2013-07', str(endyear)+'-'+str(endmonth).zfill(2)))





