import random
from compare import compareVersion
def newrandom(x,y,min,max):
    #output1 3,5  0,9

    def getRandom():
        n=(random.randint(x, y))
        s=''
        for m in range(n):
           s+=str(random.randint(min, max))+'.'
        return s[:-1]

    n=1000
    v1=[]
    v2=[]
    i=0

    while i<n:
  
        z=getRandom()
        if z not in v1:
           v1.append(z) 
        else:
           continue
        z=z[0]+'.'+getRandom()
        v2.append(z) 
        i+=1

    for i in range(n):
        print(compareVersion(v1[i], v2[i]))

#newrandom(3,5,0,9)  #output1.txt
newrandom(3,6,0,2)   #output2.tx