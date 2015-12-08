"""this module define some user-defined exceptions"""
'''Author: Muhe Xie  ID:mx419'''

# user input empty
class Empty_Input_Error(Exception):
	# raised when user input is empty
    def __str__(self):
        return 'The input is empty\n'
         
class Input_Format_Error(Exception):
	# raised when user's input's format is wrong
    def __str__(self):
        return 'The input format is wrong\n'

class Option_Input_Format_Error(Exception):
	# raised when user's input's format is wrong
    def __str__(self):
        return 'The option input format is wrong\n'

class No_Data_This_Time_Error(Exception):
	# raised when user's input's format is wrong
    def __str__(self):
        return 'There is no data for this time\n'



class station_id_out_of_range(Exception):
    
    def __str__(self):
        return 'Error: station ID does not exist.'

class day_out_of_range(Exception):
    
    def __str__(self):
        return 'Error: input day is out of range.'

class month_out_of_range(Exception):
    
    def __str__(self):
        return 'Error: input month is out of range.'