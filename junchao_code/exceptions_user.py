'''
User-defined exceptions to raise specific errors for each kind of invalid input.
'''

class station_id_out_of_range(Exception):

	def __str__(self):
		return 'Error: station ID does not exist.'

class day_out_of_range(Exception):

	def __str__(self):
		return 'Error: input day is out of range.'

class month_out_of_range(Exception):

	def __str__(self):
		return 'Error: input month is out of range.'