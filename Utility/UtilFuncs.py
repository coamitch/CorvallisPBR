# general imports

# local file imports

# utility functions for general use
def tabPrint(numTabs, message):
	# utility function to print the specified number of tabs at the beginning of the
	# message to be printed
	tabs = '\t'*numTabs
	print(f'{tabs}{message}')

def dictPrint(numTabs, dictionary: dict, currLayer=0, maxLayer=1):
	# prints all the keys down to a specified layer for any provided dictionary

	# checking if the current layer exceeds the max layer
	if currLayer > maxLayer:
		return

	# iterating through all the keys for the current layer
	for key, value in dictionary.items():
		# checking if the current key is associated with a dictionary
		if isinstance(value, dict):
			# if the current value is a dictionary, we print the key and make a
			# recursive call on the contained dictionary
			tabPrint(numTabs, f'{key}:')
			dictPrint(numTabs+1, value, currLayer+1, maxLayer=maxLayer)

		else:
			# otherwise, we print the key and its associated value
			tabPrint(numTabs, f'{key}: {value}')