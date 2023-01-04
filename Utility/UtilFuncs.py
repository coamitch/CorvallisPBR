# general imports
import platform

# local file imports
from Utility import Constants as const

# initialized variables
def isWindows():
	systemType = platform.system()
	if systemType == 'Windows':
		return True
	else:
		return False

def isLinux():
	systemType = platform.system()
	if systemType == 'Linux':
		return True
	else:
		return False

def tabPrint(numTabs, message):
	# utility function to print the specified number of tabs at the beginning of the
	# message to be printed
	tabs = '\t'*numTabs
	print(f'{tabs}{message}')

def dictPrint(numTabs, dictionary: dict, currLayer=0):
	# prints all the keys down to a specified layer for any provided dictionary

	# checking if the current layer exceeds the max layer
	if currLayer > const.maxLayer:
		return

	# iterating through all the keys for the current layer
	for key in dictionary.keys():
		# print the key
		tabPrint(numTabs, f'{key}')

		# checking if the current key is associated with a dictionary
		if isinstance(dictionary[key], dict):
			# recursive call for the next layer if a dictionary in the current layer is
			# encountered.
			dictPrint(numTabs+1, dictionary[key], currLayer+1)