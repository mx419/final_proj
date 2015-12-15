import pandas as pd
import numpy as np
import math
import sys
import mapplot
import warnings
from user_defined_exceptions import *
from frequency_statistics import FrequencyStatistics
import matplotlib.pyplot as plt
import plottingTool as vs
import prediction_and_recommendation as pr
from matplotlib.gridspec import GridSpec
import general_functions as gf
import freq_station as fs

def get_data_and_dictionary_main_function():

    print 'Initializing...'
    print "Reading the data(around 2 minutes)..."
    try:   ##minor change 1208
        data = pd.read_csv('Citibike_final.csv')
        print "reading .p file..."
        station_dictionary = gf.get_dictionary('station_dictionary.p')
    except:
        print "IOERROR happens when reading the data, please make sure the datafile is downloaded and placed at the current directory"
        sys.exit()

    return data, station_dictionary

"""
This function is going to use in main program, which will generate plots for monthly citibike data.
"""
def month_analysis(data):

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
    return

def station_freq_visualization(data):
    while True:
        try:
            print "****************************************************"
            print '\nPart 2 Instruction:\n'
            print 'Please enter valid year and month from 2013/7 to 2015/10. Year format: 2015, Month format: 7'
            print 'Enter back: return to main meun.'
            print 'Enter quit: exit this program.\n'
            print "****************************************************"
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
                map_plot_obj = mapplot.MapPlot(loc_data,month,year)
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    print "Generating frequency map..."
                    map_plot_obj.draw_freq_map()
                    print "Generating high frequency map..."
                    map_plot_obj.draw_top_k_freq_map(top_choice)
                    print "Generating high heat map..."
                    map_plot_obj.draw_heat_map()


        except InvalidInputError:
            print "The input time is invalid"
    return 

def recommendation_main_function(data, station_dictionary):

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
                except InputMonthFormatError:
                    print 'The input of month has wrong format!'
                except InputDayFormatError:
                    print 'The input of day has wrong format!'
                except InputStationidOutRange:
                    print 'The station ID does not exist!'
                except InputDayOutRange:
                    print 'The day does not exist!'
                except InputMonthOutRange:
                    print 'The month does not exist!'
                    print ' Now generate the recommendation of nearest 2 available station...'

            elif x == '2':
                print 'Please enter station ID, month and day of the date to make a recommendation.'
                try:
                    station_id = raw_input('station ID?: ')
                    month = raw_input('month?: ')
                    day = raw_input('day?: ')
                    FrequencyStatistics(data, station_dictionary, station_id, month, day)
                    print ' Now generate the recommendation of nearest 2 available station...'
                    pr.station_nearest_2(data, station_dictionary, station_id, month, day)
                except InputStationidFormatError:
                    print 'The input of station id has wrong format!'
                except InputMonthFormatError:
                    print 'The input of month has wrong format!'
                except InputDayFormatError:
                    print 'The input of day has wrong format!'
                except InputStationidOutRange:
                    print 'The station ID does not exist!'
                except InputDayOutRange:
                    print 'The day does not exist!'
                except InputMonthOutRange:
                    print 'The month does not exist!'

            elif str.lower(x) == 'back' or str.lower(x) == 'b':
                break
            elif str.lower(x) == 'quit' or str.lower(x) == 'q':
                sys.exit()
            else:
                raise OptionInputError

        except OptionInputError:
           print "Invalid input"
    return 
