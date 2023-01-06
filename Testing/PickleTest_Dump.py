import pickle as pk

testDict = {'k1': 1, 'k2': 2, 'k3': {'k4': 3, 'k5': {'k7': 4, 'k8': 5}, 'k9': 6}, 'k10': 7}

pickleFile = open('testPickle.szn', 'ab')

pk.dump(testDict, pickleFile)
pickleFile.close()

