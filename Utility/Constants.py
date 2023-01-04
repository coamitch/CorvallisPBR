# general imports

# local file imports
import Utility.UtilFuncs as uf

# TODO: windows might handle forward slashes properly. should try to eliminate this
# 	conditional block if possible.
# bracket directory paths
if uf.isWindows():
	shelveDirPath = f'\\Shelves\\'
elif uf.isLinux():
	shelveDirPath = f'Shelves/'
else:
	shelveDirPath = None

# start gg api constants needed for get requests
apiVersion = 'alpha'
startGGToken = '083f5005592a217264a5f4ec75026e5b'
ownerID = 'a5893a6f'

# max layer to print down to for a dictionary
maxLayer = 1

