"""this module define some user-defined exceptions"""
'''Author: Muhe Xie  ID:mx419'''

# user input empty

         

class OptionInputError(Exception):
	# raised when user's input's format is wrong
    def __str__(self):
        return 'The option input format is wrong\n'


class InvalidInputError(Exception):
    # raised when user's input's format is wrong
    def __str__(self):
        return 'The input is invalid'


class InputStationidFormatError(Exception):
    
    def __str__(self):
        return 'The input of station id has wrong format.'


class InputMonthFormatError(Exception):
    
    def __str__(self):
        return 'The input of month has wrong format.'

class InputDayFormatError(Exception):
    
    def __str__(self):
        return 'The input of day has wrong format.'


class InputStationidOutRange(Exception):
    
    def __str__(self):
        return 'The station ID does not exist.'

class InputDayOutRange(Exception):
    
    def __str__(self):
        return 'Input day is out of range.'

class InputMonthOutRange(Exception):
    
    def __str__(self):
        return 'Input month is out of range.'