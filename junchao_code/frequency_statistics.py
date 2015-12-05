import math
import pandas as pd
import numpy as np
from collections import Counter

# DS-GA 1007 Final Project
# Station frequency statistics on historical data
# Author: Junchao Zheng

class FrequencyStatistics():
	'''
	The FrequencyStatistics class generates several attributes including:
	Station ID, the month and day of a particular date; predifined data and station dictionary.
	In the class we handle exceptions and raise certain user-defined exceptions when invalid input is given.
	And three functions under the class to calculate statistics of the usage of the given station on the given date, the usage of the given station over all dates and the usage of all stations over all dates respectively.
	Statistics of the usage includes median and percentile at 0.8.
	'''

	def __init__(self, data, station_dictionary, station_id, month, day):

		# Lists of month with 31 or 30 days
		MONTH_31DAYS = [1, 3, 5, 7, 8, 10, 12]  
		MONTH_30DAYS = [2, 4, 6, 9, 11]

		# Input dataset cover all historical data.
		self.data = data
		self.station_dictionary = station_dictionary

		# Check input for station_id, month and day has right format, else raise error.
		try:
			int(station_id)
		except ValueError:
			print 'Invalid input format for station ID!'

		try:
			int(month)
		except ValueError:
			print 'Invalid input format for month!'

		try:
			int(day)
		except ValueError:
			print 'Invalid input format for day!'

		# Check input for station_id within right range, else raise error.
		if station_id not in station_dictionary.keys():
			raise station_id_out_of_range()
		else:
			self.station_id = int(station_id)  # self.station_id has int format.

		# Check input for month, day within right range, else raise error respectively.
		# self.month and self.day has int format.
		if int(month) in MONTH_31DAYS:  # For month which has 31 days.
			if int(day) < 1 or int(day) > 31:
				raise day_out_of_range()
			else:
				self.day = int(day)
			self.month = int(month)
		elif int(month) in MONTH_30DAYS:  # For month which has 30 days. 
			if int(day) < 1 or int(day) > 30:
				raise day_out_of_range()
			else:
				self.day = int(day)
			self.month = int(month)
		else:
			raise month_out_of_range()

	def _usage_station_allyear(self):
		'''Function to generate statistics of usage of all stations over all dates.'''
		freq_station_allyear = Counter(self.data['start station id'])
		freq_allyear_values = np.array(freq_station_allyear.values())
		number_of_day = len(self.data['startdate'].unique())
		return np.median(freq_allyear_values)/number_of_day, np.percentile(freq_allyear_values, 80)/number_of_day

	def _usage_station_day_given(self):
		'''Function to generate statistics of usage of given station on given date.'''

		data_station_given = data[data['start station id'] == self.station_id]
		data_station_month = data_station_given[data_station_given['startmonth'] == self.month]
		data_station_day = data_station_month[data_station_month['startday'] == self.day]
		return data_station_day.shape[0]/len(data_station_day['startyear'].unique())

	def _usage_station_given(self):
		'''Function to generate statistics of usage of given station over all dates.'''

		data_station_given = self.data[self.data['start station id'] == self.station_id]
		freq_station_given = Counter(data_station_given['startdate'])
		return np.median(np.array(freq_station_given.values())), np.percentile(np.array(freq_station_given.values()), 80)

		