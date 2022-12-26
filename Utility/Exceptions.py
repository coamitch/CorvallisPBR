class CommandError(Exception):
	# raised when an invalid command is issued
	pass

class ArgsError(Exception):
	# raised when there are too few or too many arguments provided to the command
	pass

class SaveError(Exception):
	# raised when there is no file stored to save
	pass