import pandas as pd
import numpy as np
import math
import operator
import sys
import re 
from user_defined_exceptions import *
import mapplot #plot map
import warnings
import general_functions as gf
import freq_station as fs
import option_functions as op


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
    
    data, station_dictionary = op.get_data_and_dictionary_main_function()
    
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
                    op.month_analysis(data)

                elif main_option == '2':
                    op.station_freq_visualization(data)

                else:  
                    op.recommendation_main_function(data, station_dictionary)

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