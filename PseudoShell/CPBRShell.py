import shelve

from Exceptions import *
from Utility import QueryLibrary as ql
from Utility import Constants as const

class CPBRShell():
	# constructor
	def __init__(self):
		self.currTournament = None

		self.switch = dict()
		self.switch['load'] = self.load
		self.switch['save'] = self.save
		# self.switch['reset'] =

	# member methods
	def checkArgs(self, numArgs, args: list):
		# checking if the args list is the correct length
		if numArgs == len(args):
			# if it has the correct number of arguments, return true
			# the main assumption here is that the arg values are correct
			return True

		# otherwise there are too few or too many arguments, and we return false
		return False

	def load(self, args: list):
		# loads a tournament into the current working tournament slot.
		# args:	- event id

		# checking if we have the correct number of args
		if not self.checkArgs(1, args):
			raise ArgsError

		# if we have the correct arguments, we unpack them
		eventID = int(args[0])

		# loading the tournament into a new dictionary
		tournamentDict = dict()
		ql.updateTournamentDict(eventID, tournamentDict)

		self.currTournament = tournamentDict

		print(f'\tTournament loaded into working slot.')

	def reset(self):
		# re-initializes the shell variables to their starting state
		self.currTournament = None

	def save(self, args: list):
		# saves (serializes) the current working tournament. file path preset.
		# args:	- shelve name (excluding the dir path)
		#		- key used for the shelve

		# checking if we have the correct number of args
		if not self.checkArgs(2, args):
			raise UserWarning

		# if we have the correct arguments, we unpack them
		shelveName = args[0]
		tournamentKey = args[1]

		# checking that we have something to save
		if not self.currTournament:
			raise SaveError

		# otherwise we have the correct number of arguments and we need to save the
		# current tournament (i.e. serialize it)
		shelvePath = f'{const.shelveDirPath}{shelveName}'
		workingShelve = shelve.open(shelvePath)

		# saving the current tournament into the shelve
		workingShelve[tournamentKey] = self.currTournament

		# closing the opened shelve
		workingShelve.close()

		print(f'\tTournament saved to {shelvePath} under key name "{tournamentKey}".')

if __name__ == '__main__':
	# creating a basic shell object
	shellObj = CPBRShell()

	# printing help menu
	print('Please enter one of the commands below (comma separated):')
	print('\t- load(event ID)')
	print('\t- save(shelve name, tournament name)')

	print('\n\t- * <--- issues the previous command')
	print('\t- reset <--- resets all current working variables')
	print('\t- exit <--- terminates the program')

	print('\n\tUsage: function,arg1,arg2,arg3,...')
	print('************************************************************************')

	# starting endless loop so the user can keep entering commands
	done = False
	first = True
	while not done:
		# prompting the user to input a command
		inputStr = input('@ ')

		if inputStr == '*':
			if first:
				print('\tNeed to enter a command before using *.')
				continue
			else:
				inputStr = prevInputStr

		argsList = inputStr.split(',')
		func = argsList[0]
		argsList.remove(argsList[0])

		if func == 'exit':
			print('Exit...')
			done = True
		else:
			try:
				shellObj.switch[func](argsList)
				prevInputStr = inputStr

				if first:
					first = False
			except CommandError:
				# function doesn't exist
				print('\tCommand not found. Please verify with the list above.')
				print('\tUsage: function,arg1,arg2,arg3,...')

			except ArgsError:
				print('\tToo few or too many arguments. Please verify with the list above.')
				print('\tUsage: function,arg1,arg2,arg3,...')

			except SaveError:
				print('\tPlease load a tournament before attempting to save.')