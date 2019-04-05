import random
from overlap import isOverlapR2
def newrandom():
    '''
    used to generate sample and process some controled testing
    '''
    def getRandom(min,max):
        for m in range(2):
           (a,b)=random.randint(min, max),random.randint(min, max)
           (c,d)=random.randint(min, max),random.randint(min, max)
        return (a,b), (c,d)

    n=100
    v1=[]
    v2=[]
    i=0
    while i<n:
        #-5,5  ==>output1.txt
        #-10,0 ==>output2.txt
        #0,100 ==> output3.txt
        (a,b), (c,d)=getRandom(-20,20)  
        v1.append((a,b))
        v2.append((c,d))
        i+=1
    
    for i in range(n):
        print(v1[i], v2[i],isOverlapR2(v1[i], v2[i]))
    
    '''
    #used to generate testsample.txt
    print (n+1)
    for i in range(n):
        print(v1[i][0],',', v1[i][1], ',', v2[i][0], ',', v2[i][1] )
    '''
newrandom()
