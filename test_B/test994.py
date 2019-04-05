import random
from compare import compareVersion
def newrandom(x,y,min,max):

    def getRandom():
        vector="!@#$%¨&*()[}]{´`~^ç?/;:.>,<\|"
        vectorLen=len(vector)
        newVector=[vector[i:i+1] for i in range(0, vectorLen, 1)]
        n=(random.randint(x, y))
        s=''
        for m in range(n):
            if m%2==0:
               s+=str(random.randint(min, max))+'.'
            else:
               number=random.randint(0, vectorLen-1)
               s+=newVector[number]+'.'
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
        
        v1.append(z) 
        z=z[0]+'.'+getRandom()
        v2.append(z) 
        i+=1

    for i in range(n):
        print(compareVersion(v1[i], v2[i]))

newrandom(3,6,0,2)   #output3.tx