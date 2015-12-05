import pickle

'''to merge with other teammates'''

def get_dictionary(filename):
	'''The function takes a dictionray.p file as input and returns a dictionary.'''
	
	dictionary = pickle.load(open(filename, 'rb'))
	return dictionary 

