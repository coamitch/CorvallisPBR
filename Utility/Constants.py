# general imports

# local file imports
import Utility.UtilFuncs as uf

# bracket directory paths
if uf.isWindows():
	bracketDirPath = f'..\\Brackets\\'
elif uf.isLinux():
	bracketDirPath = f'../Brackets/'
else:
	bracketDirPath = None

apiVersion = 'alpha'
startGGToken = '083f5005592a217264a5f4ec75026e5b'
ownerID = 'a5893a6f'

