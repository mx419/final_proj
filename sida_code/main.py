from __future__ import division
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import operator
import sys
import visualizationTool as pievis
from visualizationTool import *


# DS-GA 1007
# Main program
# Author: Sida Ye


# need to modify
"""
This program was created to help users identify public Wi-Fi locations that are closest to an address-of-interest.
To do so, the user provides an address in NYC, including all 5 boroughs. 
The program analyzes the address and presents the 5 nearest Wifi hot-spots to the user in table and map format. 
The table output includes the following information about the WiFi spot: Name, Location, Location Type, SSID, WiFi Type, and Distance. To help to user locate these hot-spots easily, a map is provided with markers to indicate both the address the user searched for (in blue), and the locations of the hot-spots (red) numbered in the same order as the table. To help the user better understand the distribution of WiFi spots in the city,
the program also produces and saves several figures displaying statistics about the free Wifi locations in NYC.
"""

def main():
	print 'Initilizing.......'
		# data import 
	try:
		while True:
			print '\n You have several options'
			print '\n 1. Please input year and month to see plots'
			print '\n 2. Please enter start date and end date to see plots'
			print '\n 3. Please enter quit to exit this program\n'
			x = raw_input()
			if x == '1':
				year = int(raw_input('year?: '))
				month = int(raw_input('month?: '))
				variable = raw_input('gender or usertype: ')
				data = pd.read_csv('../data/{}-{} - Citi Bike trip data.csv'.format(str(year), str(month).zfill(2)))
				pievis.pieplot(data, year, month, year, month, variable)
				plt.show()

			elif x == 'quit':
				sys.exit()

	# 		elif re.match(r"^[0-9]{4}$", x):
	# 			try:
	# 				plot_income_by_yr(int(x))
	# 			except KeyError:
	# 				print '\n Input Error: Invalid Year!\n'

	# 		else:
	# 			print "\n Input Error: Please a valid year!\n"

	# # Q8
	# 	print '\n Generating plots......'
	# 	yr_list = range(2007, 2013)
	# 	for yr in yr_list:
	# 		result = vs.visualize_tool(yr)	# use visulize tool class to generate plot
	# 		result.plot_boxplot()
	# 		result.plot_hist()
	# 	print '\n Plots are saved at current dictionary'

	except KeyboardInterrupt, ValueError:
		print "\n Interrupted!"
	except ArithmeticError, OverflowError:
		print "\n Math Error"
	except ZeroDivisionError:
		print "\n Math Error"
	except TypeError:
		print "\n Type Wrong!"
	except EOFError:
		print "\n Interrupted!"

	
# Q9



if __name__ == '__main__':
	main()




