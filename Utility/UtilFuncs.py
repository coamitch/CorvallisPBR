# general imports
import platform

# local file imports

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