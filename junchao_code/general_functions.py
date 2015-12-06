import pickle

'''to merge with other teammates'''

def get_dictionary(filename):
	'''The function takes a dictionray.p file as input and returns a dictionary.'''
	
	dictionary = pickle.load(open(filename, 'rb'))
	return dictionary 

def data_extract(data, startyear, startmonth, startday, endyear, endmonth, endday):
    
    data_by_year_start = data.loc[data['startyear'] == startyear]
    data_by_month_start = data_by_year_start[data_by_year_start['startmonth'] == startmonth]
    data_by_day_start = data_by_month_start[data_by_month_start['startday'] == startday]
    startindex = data_by_day_start.index[0]
    
    data_by_year_end = data.loc[data['startyear'] == endyear]
    data_by_month_end = data_by_year_end[data_by_year_end['startmonth'] == endmonth]
    data_by_day_end = data_by_month_end[data_by_month_end['startday'] == endday]
    endindex = data_by_day_end.index[-1]
    
    return data.ix[startindex:endindex, :]