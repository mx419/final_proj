import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import operator
import sys
import re 
import pickle
from user_defined_exceptions import *
import mapplot #plot map
import warnings
import plottingTool as vs
import general_functions as gf
import freq_station as fs
from frequency_statistics import FrequencyStatistics
from prediction_and_recommendation import *
from matplotlib.gridspec import GridSpec


# DS-GA 1007
# Main program
# Author: Sida Ye, Junchao Zheng, Muhe Xie


# need to modify
"""
This program was created to help users identify public Wi-Fi locations that are closest to an address-of-interest.
To do so, the user provides an address in NYC, including all 5 boroughs. 
The program analyzes the address and presents the 5 nearest Wifi hot-spots to the user in table and map format. 
The table output includes the following information about the WiFi spot: Name, Location, Location Type, SSID, WiFi Type, and Distance. To help to user locate these hot-spots easily, a map is provided with markers to indicate both the address the user searched for (in blue), and the locations of the hot-spots (red) numbered in the same order as the table. To help the user better understand the distribution of WiFi spots in the city,
the program also produces and saves several figures displaying statistics about the free Wifi locations in NYC.
"""

def main():
    print 'Initilizing...'
    print "Reading the data..."
    data = pd.read_csv('Citibike_final.csv')

    print "reading .p file..."
    station_dictionary = gf.get_dictionary('station_dictionary.p')
        # import initialize code 
    while True:
        try:
            print '\n You have several options. Enter 1 or 2 or 3 to choose your option, enter quit to exit the program'
            print '\n Option 1: Check sida \'s function '
            print '\n Option 2: Check frequency result'
            print '\n Option 3: Check prediction result'
            main_option= raw_input("Your option:")
            if not re.match('([123]|exit)$',main_option):
                raise Option_Input_Format_Error
            else:
                print "start"

                if main_option == 'quit':
                    print "Thanks for using, bye"
                    sys.exit()

                elif main_option == '1':
                    #insert sida's code here
                    while True:



                        print 'Please enter valid year and month'
                        year = int(raw_input('year? '))
                        month = int(raw_input('month?'))
                        data_month = gf.data_extract(data, year, month, year, month)
                        object_plot = vs.visualizationTool(data_month, year, month)
                        object_plot.pieplot('gender')
                        object_plot.pieplot('usertype')
                        object_plot.plot_daily_freq(show_mile=False)
                        object_plot.plot_daily_freq(show_mile=True)



                    
                elif main_option == '2':
                    
                    print 'Please enter valid year and month'
                    year = 2014
                    month = 1
                    top_choice = 5

                    data_month = gf.data_extract(data, year, month, year, month)
                   

                    loc_data = fs.station_info(data_month, year, month)
                    print fs.high_freq_station(loc_data, top_choice)
                    map_plot_obj = mapplot.MapPlot(loc_data,1)
                    with warnings.catch_warnings():
                        warnings.simplefilter("ignore")
                        map_plot_obj.draw_freq_map()
                        map_plot_obj.draw_top_k_freq_map(5)
                        map_plot_obj.draw_heat_map()
                    
                    #while True:
                    #   try:
                    #       print "Please enter the year and month,or enter quit to go to the main menu"
                    #       print "Our data only cover 2013.7 to 2015.10, please enter in that range"
                    #       year = raw_input("Year?:")
                    #       if not re.match('((201[345])|(exit))$',year):
            #                   raise Option_Input_Format_Error
            #               if year == 'quit':
            #                   break
            #               year = int(year)
            #               if year == 2013:
            #                   month = raw_input("month?:")
            #                   if not re.match('(7|8|9|10|11|12|quit)',month):
            #                       raise Option_Input_Format_Error
            #                   if month == 'quit':
            #                       break
            #                   month = int(month)
            #               elif year == 2014:
            #                   month = raw_input("month?:")
            #                   if not re.match('(1|2|3|4|5|6|7|8|9|10|11|12|quit)',month):
            #                       raise Option_Input_Format_Error
            #                   if month == 'quit':
            #                       break
            #                   month = int(month)
            #               else:
            #                   month = raw_input("month?:")
            #                   if not re.match('(1|2|3|4|5|6|7|8|9|10|quit)',month):
            #                       raise Option_Input_Format_Error
            #                   if month == 'quit':
            #                       break
            #                   month = int(month)


                    #   except Option_Input_Format_Error:
                    #       print "Invalid input, please enter again\n"



                else:  #main_option  = 3
                #insert junchao's prediction
                    while True:
                        print '\n You have several options. Enter 1, 2 or 3.'
                        print '\n 1. You can explore the use of a station on a particular day and get advice.'
                        print '\n 2. When you find a station is empty, try this option to recommend alternatives within 15-minute walk.'
                        print '\n 3. Please enter quit to exit this prediction program.'
                        x = raw_input()
                        if x == '1':
                            station_id = raw_input('station ID?: ')
                            month = raw_input('month?: ')
                            day = raw_input('day?: ')
                            prediction_result = prediction_function(data, station_dictionary, station_id, month, day)
                            prediction_statement(prediction_result)
                        elif x == '2':
                            station_id = raw_input('station ID?: ')
                            month = raw_input('month?: ')
                            day = raw_input('day?: ')
                            station_nearest_5(data, station_dictionary, station_id, month, day)
                        elif x == 'quit':
                            break
                    


        except Option_Input_Format_Error:
            print "Invalid input"




if __name__ == '__main__':
    main()
