import shelve

from Utility.Exceptions import *
from Utility import QueryLibrary as ql
from Utility import Constants as const
from Utility.UtilFuncs import *

class CPBRShell():
	# constructor
	def __init__(self):
		self.shellVars = dict()

		self.switch = dict()
		self.switch['load_tournament'] = self.loadTournament
		self.switch['load_shelve'] = self.loadShelve
		self.switch['save'] = self.save
		self.switch['reset'] = self.reset
		self.switch['vars'] = self.printVars
		self.switch['view_shelve'] = self.viewShelve

	# member methods
	def checkArgs(self, numArgs, args: list):
		# checking if the args list is the correct length
		if numArgs == len(args):
			# if it has the correct number of arguments, return true
			# the main assumption here is that the arg values are correct
			return True

		# otherwise there are too few or too many arguments, and we return false
		return False

	def loadTournament(self, args: list):
		# loads a tournament into the current working tournament slot.
		# args:	- event id

		# checking if we have the correct number of args
		if not self.checkArgs(1, args):
			raise ArgsError

		# if we have the correct arguments, we unpack them
		eventID = int(args[0])

		# loading the tournament into a new dictionary
		tournamentDict, tournamentName, eventName = ql.unpackTournament(eventID)

		# loading tournament into the shell vars dictionary
		self.shellVars['tournamentDict'] = tournamentDict
		self.shellVars['tournamentName'] = tournamentName
		self.shellVars['eventName'] = eventName

		self.printVars([])

	def loadShelve(self, args: list):
		# loads a tournament into the current working tournament slot from the specified
		# shelve and entries
		# args:	- shelve name
		#		- tournament name
		# 		- event name

		# checking if we have the correct number of args
		if not self.checkArgs(3, args):
			raise ArgsError

		# if we have the correct arguments, we unpack them
		shelveName = args[0]
		tournamentName = args[1]
		eventName = args[2]

		# opening the shelve
		shelvePath = f'{const.shelveDirPath}{shelveName}'
		workingShelve = shelve.open(shelvePath)

		# attempting to "get" the tournament and event specified
		tempGetRslt = workingShelve.get(tournamentName)

		if tempGetRslt == None:
			raise EmptyEntryError

		tournamentDict = tempGetRslt.get(eventName)

		if tournamentDict == None:
			raise EmptyEntryError

		# loading tournament into the shell vars dictionary
		self.shellVars['tournamentDict'] = tournamentDict
		self.shellVars['tournamentName'] = tournamentName
		self.shellVars['eventName'] = eventName

		# printing the variables we just loaded
		self.printVars([])

	def printVars(self, args: list):
		# prints all current working variables local to the shell
		# args:	- none

		# checking if we have the correct number of args
		if not self.checkArgs(0, args):
			raise ArgsError

		# otherwise we have the correct number of arguments and we can print the current
		# working variables
		for key, value in self.shellVars.items():
			if isinstance(value, dict):
				tabPrint(1, f'{key} - # sets played: {len(value.keys())}')
			else:
				tabPrint(1, f'{key} - {value}')

	def reset(self):
		# re-initializes the shell variables to their starting state (empty dictionary)
		self.shellVars = dict()

	def save(self, args: list):
		# saves (serializes) the current working tournament. file path preset.
		# args:	- shelve name (excluding the dir path)
		#		- key used for the shelve

		# checking if we have the correct number of args
		if not self.checkArgs(1, args):
			raise UserWarning

		# if we have the correct arguments, we unpack them
		shelveName = args[0]
		tournamentDict = self.shellVars['tournamentDict']
		tournamentName = self.shellVars['tournamentName']
		eventName = self.shellVars['eventName']

		# checking that we have something to save
		if not (tournamentDict or tournamentName or eventName):
			raise SaveError

		# otherwise we have the correct number of arguments and we need to save the
		# current tournament (i.e. serialize it)
		shelvePath = f'{const.shelveDirPath}{shelveName}'
		workingShelve = shelve.open(shelvePath)

		# retrieving the tournament dictionary and event dictionary
		tournShelveDict = workingShelve.get(tournamentName, dict())

		# loading the tournament dictionary and storing back into the shelve
		tournShelveDict[eventName] = tournamentDict
		workingShelve[tournamentName] = tournShelveDict

		# closing the opened shelve
		workingShelve.close()

		tabPrint(1, f'\tTournament saved to {shelvePath} under key name "{tournamentName}/{eventName}".')

	def viewShelve(self, args: list):
		# loads a shelve entry into the current working tournament slot.
		# args:	- shelve name

		# checking if we have the correct number of args
		if not self.checkArgs(1, args):
			raise ArgsError

		# if we have the correct arguments, we unpack them
		shelveName = args[0]

		# opening shelve
		shelvePath = f'{const.shelveDirPath}{shelveName}'
		workingShelve = shelve.open(shelvePath)

		dictPrint(1, workingShelve)

		workingShelve.close()

if __name__ == '__main__':
	# creating a basic shell object
	shellObj = CPBRShell()

	# printing help menu
	tabPrint(0, 'Please enter one of the commands below (comma separated):')
	tabPrint(1, '- load_tournament(event ID)')
	tabPrint(1, '- load_shelve(shelve name, tournament name, event name)')
	tabPrint(1, '- save(shelve name)')
	tabPrint(1, '- vars()')
	tabPrint(1, '- view_shelve(shelve name)')

	tabPrint(0, ' ') # just a space in between the general commands and help commands

	tabPrint(1, '- * <--- issues the previous command')
	tabPrint(1, '- help <--- lists what each command does')
	tabPrint(1, '- reset <--- resets all current working variables')
	tabPrint(1, '- exit <--- terminates the program')

	tabPrint(1, '\nUsage: function,arg1,arg2,arg3,...')
	tabPrint(0, '************************************************************************')

	# starting endless loop so the user can keep entering commands
	done = False
	first = True
	while not done:
		# prompting the user to input a command
		inputStr = input('@ ')

		if inputStr == '*':
			if first:
				tabPrint('\tNeed to enter a command before using *.')
				continue
			else:
				inputStr = prevInputStr

		argsList = inputStr.split(',')
		func = argsList[0]
		argsList.remove(argsList[0])

		if func == 'exit':
			tabPrint(0, 'Exit...')
			done = True
		else:
			try:
				shellObj.switch[func](argsList)
				prevInputStr = inputStr

				if first:
					first = False
			except CommandError:
				# function doesn't exist
				tabPrint(1, 'Command not found. Please verify with the list above.')
				tabPrint(1, 'Usage: function,arg1,arg2,arg3,...')

			except ArgsError:
				tabPrint(1, 'Too few or too many arguments. Please verify with the list above.')
				tabPrint(1, 'Usage: function,arg1,arg2,arg3,...')

			except SaveError:
				tabPrint(1, 'Please load a tournament before attempting to save.')

			except EmptyEntryError:
				tabPrint(1, 'No entry found. Please try again, or verify the entry exists.')

