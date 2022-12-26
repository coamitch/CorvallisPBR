# general imports

# local file imports
import Utility.UtilFuncs as uf

# bracket directory paths
if uf.isWindows():
	shelveDirPath = f'..\\Shelves\\'
elif uf.isLinux():
	shelveDirPath = f'../Shelves/'
else:
	shelveDirPath = None

apiVersion = 'alpha'
startGGToken = '083f5005592a217264a5f4ec75026e5b'
ownerID = 'a5893a6f'

