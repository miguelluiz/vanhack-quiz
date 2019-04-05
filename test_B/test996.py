from compare import compareVersion
'''
checking python packages 
'''

arq1='r1.txt'
arq2='r2.txt'

def loadFile(arq):
    file=open(arq,'r')
    return file.readlines()

dataA=loadFile(arq1)
dataB=loadFile(arq2)
for i in range(len(dataA)):
    print(compareVersion(dataA[i], dataB[i]))
