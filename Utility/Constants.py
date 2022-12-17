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

