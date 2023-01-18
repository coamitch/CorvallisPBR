import pickle as pk

pickleFile = open('testPickle.szn', 'rb')
pickleDict = pk.load(pickleFile)

print(pickleDict)

pickleFile.close()