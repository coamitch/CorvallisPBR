# general imports
import pickle as pk
import os

# class to use in place of shelve or directly working with pickle
class PickleShelve():
	# constructor/destructor
	def __init__(self, filePath, fileName):
		# storing attributes of the class
		self._filePath = filePath
		self._fileName = fileName

		# loading the pickle dictionary from the specified file
		self._load()

	# getters/setters
	@property
	def filePath(self):
		return self._filePath

	@property
	def fileName(self):
		return self._fileName

	@property
	def pickleDict(self):
		return self._pickleDict
		
	# general methods
	def save(self, args=None):
		# saves the current dictionary back into the file specified on object creation.
		# returns true if successful, returns false otherwise

		# checking if the user provided a list of arguments
		if args:
			# if they did, we unpack them and replace the file path and file name
			# attributes before the file open
			self._filePath = args[0]
			self._fileName = args[1]

		# opening the file to write (not append)
		pickleFile = open(f'{self._filePath}/{self._fileName}', 'wb')

		# dumping the current dictionary into the file
		pk.dump(self._pickleDict, pickleFile)

		# closing the file. no need to reload the file at the end since the dictionary
		# remains in the class and can continue being updated.
		pickleFile.close()

	def add(self, key, value):
		# adds an entry into the current dictionary. returns true if successful, returns
		# false if the addition failed.

		# checking if the key already exists
		if self._pickleDict.get(key) != None:
			# the key already exists in the dictionary, so we return false
			return False

		# otherwise we can assume the key doesn't exist in the current dictionary and
		# we can proceed with the addition
		self._pickleDict[key] = value
		return True

	def _load(self, args=None):
		# checking if the user provided a list of arguments
		if args:
			# if they did, we unpack them and replace the file path and file name
			# attributes before the file open
			self._filePath = args[0]
			self._fileName = args[1]

		# checking if the file specified exists
		if not os.path.isfile(f'{self._filePath}/{self._fileName}'):
			# if the file isn't there, then we just set the pickleDict attribute to an
			# empty dictionary (i.e. no need to open or load the data via pickle).
			self._pickleDict = dict()
			return

		# otherwise the file exists and we can load in the data that it contains
		pickleFile = open(f'{self._filePath}/{self._fileName}', 'rb')
		self._pickleDict = pk.load(pickleFile)

		# given that this is supposed to mimic a shelve, we check to make sure that the
		# object loaded is in fact a dictionary
		if not isinstance(self.pickleDict, dict):
			# if it isn't, we load an empty dictionary
			self._pickleDict = dict()

		# now that we have loaded the data we want, we need to close the file for later
		pickleFile.close()
