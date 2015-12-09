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
import prediction_and_recommendation as pr
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
    print 'Initializing...'
    print "Reading the data(around 2 minutes)..."
    try:   ##minor change 1208
        data = pd.read_csv('Citibike_final.csv')
        print "reading .p file..."
        station_dictionary = gf.get_dictionary('station_dictionary.p')
    except:
        print "IOERROR happens when reading the data, please make sure the datafile is downloaded and placed at the current directory"
        sys.exit()
        # import initialize code 
    while True:
        try:
            print "Main Menu:\n"
            print '\n You have several options. Enter 1 or 2 or 3 to choose your option, enter quit to exit the program'
            print '\n Option 1: Check sida \'s function '
            print '\n Option 2: Check frequency result'
            print '\n Option 3: Check prediction result'
            main_option= raw_input("Your option:")
            if not re.match('([123]|quit)$',main_option):
                raise OptionInputError
            else:
                print "Starting..."

                if main_option == 'quit':
                    print "Thanks for using, bye."
                    sys.exit()

                elif main_option == '1':
                    #insert sida's code here
                    while True:
                        print '\nPart 1 Instruction:\n'
                        print 'Please enter valid year and month from 2013/7 to 2015/10. Year format: 2015, Month format: 7'
                        print 'Enter back: return to main meun.'
                        print 'Enter quit: exit this program.\n'
                        year = raw_input('year? ')
                        if year == 'quit':
                            sys.exit()
                        elif year == 'back':
                            break
                        month = raw_input('month? ')
                        if month == 'quit':
                            sys.exit()
                        elif month == 'back':
                            break
                        if gf.check(year, month):
                            year_int = int(year)
                            month_int = int(month)
                            print 'Please wait.......'
                            data_month = gf.data_extract(data, year_int, month_int, year_int, month_int)
                            object_plot = vs.visualizationTool(data_month, year_int, month_int)
                            print 'Generating gender distribution pie plot...'
                            object_plot.pieplot('gender')
                            print 'Generating usertype distribution pie plot...'
                            object_plot.pieplot('usertype')
                            print 'Generating daily usage plot...'
                            object_plot.plot_daily_freq(show_mile=False)
                            print 'Generating daily miles plot...'
                            object_plot.plot_daily_freq(show_mile=True)
                        else:
                            print '\nError: Please enter valid year and month!'



                elif main_option == '2':
                    
                    while True:
                        try:
                            print '\nPart 2 Instruction:\n'
                            print 'Please enter valid year and month from 2013/7 to 2015/10. Year format: 2015, Month format: 7'
                            print 'Enter back: return to main meun.'
                            print 'Enter quit: exit this program.\n'
                            year = raw_input('year? ')
                            if year == 'back':
                                break
                            if year == 'quit':
                                sys.exit()
                            month = raw_input('month?')
                            if month == 'back':
                                break
                            if month == 'quit':
                                sys.exit()
                            if not gf.check(year,month):
                                raise InvalidInputError
                            else:
                                month = int(month)
                                year = int(year)
                                top_choice = 5 #shouw top 5 stations
                                data_month = gf.data_extract(data, year, month, year, month)
                                print "Calculating top 5 high frequency station..."
                                loc_data = fs.station_info(data_month, year, month)
                                print "Show top 5 high frequency station:"
                                stat_list = fs.high_freq_station(loc_data, top_choice)
                                print stat_list
                                gf.show_map(stat_list)
                                map_plot_obj = mapplot.MapPlot(loc_data,1)
                                with warnings.catch_warnings():
                                    warnings.simplefilter("ignore")
                                    print "Generating frequency map..."
                                    map_plot_obj.draw_freq_map()
                                    print "Generating high frequency map..."
                                    map_plot_obj.draw_top_k_freq_map(top_choice)
                                    print "Generating high heat map..."
                                    map_plot_obj.draw_heat_map()

                        except InvalidInputError:
                            print "The input time is invalid" # change later


                else:  #main_option  = 3
                #insert junchao's prediction

                #insert junchao's prediction
                    while True:
                        print '\nPart 3 Instruction:\n'
                        print 'Please enter 1 or 2 to start the prediction or recommendation function:'
                        print 'Please enter station ID, month and day of the date to make a prediction.'
                        print 'Enter back: return to main meun.'
                        print 'Enter quit: exit this program.\n'
                        try:
                            x = raw_input()
                            if x == '1':
                                print 'Please enter station ID, month and day of the date to make a prediction.'
                                try:
                                    station_id = raw_input('station ID?: ')
                                    month = raw_input('month?: ')
                                    day = raw_input('day?: ')
                                    print ' Now generate the prediction of the usage of the station...'
                                    prediction_result = pr.prediction_function(data, station_dictionary, station_id, month, day)
                                    pr.prediction_statement(prediction_result)
                                except InputStationidFormatError:
                                    print 'The input of station id has wrong format!'
                                except InputMonthFormatError():
                                    print 'The input of month has wrong format!'
                                except InputDayFormatError():
                                    print 'The input of day has wrong format!'
                                except InputStationidOutRange():
                                    print 'The station ID does not exist!'
                                except InputDayOutRange():
                                    print 'The day does not exist!'
                                except InputMonthOutRange():
                                    print 'The month does not exist!'
                                print ' Now generate the recommendation of nearest 2 available station...'




                            elif x == '2':
                                try:
                                    station_id = raw_input('station ID?: ')
                                    month = raw_input('month?: ')
                                    day = raw_input('day?: ')
                                    FrequencyStatistics(data, station_dictionary, station_id, month, day)
                                    print ' Now generate the recommendation of nearest 2 available station...'
                                    pr.station_nearest_2(data, station_dictionary, station_id, month, day)
                                except InputStationidFormatError:
                                    print 'The input of station id has wrong format!'
                                except InputMonthFormatError():
                                    print 'The input of month has wrong format!'
                                except InputDayFormatError():
                                    print 'The input of day has wrong format!'
                                except InputStationidOutRange():
                                    print 'The station ID does not exist!'
                                except InputDayOutRange():
                                    print 'The day does not exist!'
                                except InputMonthOutRange():
                                    print 'The month does not exist!'




                            elif str.lower(x) == 'back' or str.lower(x) == 'b':
                                break
                            elif str.lower(x) == 'quit' or str.lower(x) == 'q':
                                sys.exit()
                            else:
                                raise OptionInputError
                        except OptionInputError:
                            print 'Invalid option input!'





        except OptionInputError:
            print "Invalid input"




if __name__ == '__main__':
    try:    
        main()

    except KeyboardInterrupt:
        print 'the program has been interrupted by KeyboardInterrupt, thanks for trying,Goodbye'
    except EOFError:
        print 'the program has been interrupted by EOFERROR, thanks for trying, Goodbye'
    except TypeError:
        print 'the program has been interrupted by TypeError, thanks for trying, Goodbye'
    except OverflowError:
        print 'the program has been interrupted by OverflowError, thanks for trying, Goodbye'