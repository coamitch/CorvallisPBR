from Utility.QueryLibrary import *
from Utility.Constants import *
from Utility.UtilFuncs import *

# testing constants
eventID = 828052
slug = "frt-pnch-frdy-8"

queryRslt = retrieveAttendees(slug)
queryDict = unpackAttendees(queryRslt)

tabPrint(0, f'unpacked dictionary:')
dictPrint(1, queryDict, maxLayer=5)
