from overlap import isOverlapR2
import sys
if sys.version.split(' ')[0]<'3':
    print ('Python 3 is required')
    exit()
print ('This program that accepts two lines (x1,x2) \nand (x3,x4) on the x-axis and returns whether they overlap')
print ("Enter total number of lines to check, default=1 pair to check")
i = 0
n = input()
if n is None or len(n)==0: 
   n=1
else:
   n=int(n)
v1=[]
v2=[]
print ('please add ',n,'lines to be checked - use comma')
print ('(1,2),(3,4) should be typed as 1,2,3,4')
while i < n:
    keys = input()
    if len(keys.split(','))==4 and keys.split(',').count('')==0:
        (a,b), (c,d) = keys.split(',')[0:2], keys.split(',')[2:4]
        v1.append((float(a), float(b)))
        v2.append((float(c), float(d)))
        i+=1
    else:
        print('invalid data:\nit is required 4 values - \nplease include "," between the numbers')
for i in range(n):
        print(v1[i], v2[i],isOverlapR2(v1[i], v2[i]))
'''
for i in range(n):
    print ('Enter line ',k,':')
    k+=1
    (a,b) = input().split(',')
    print ('Enter line ',k,':')
    k+=1
    (c,d) = input().split(',')
    (a,b), (c,d)= (float(a), float(b)), (float(c), float(d))
    print ('checking wheter they overlap or not...')
    check=isOverlapR2((a,b),(c,d))
    print ('line: ',(a,b),'and', 'line:', (c,d) ,end='')
    if check: 
        print (' do overlap')
    else:
        print (' do not overlap')
'''

'''
while i <n
    keys = input()
    if keys.split(',')==4:
        print (keys)
        (a,b), (c,d) = keys.split(',')[0:2], keys.split(',')[2:4]
        print ((a,b), (c,d))
        quit()
        print ('A=',A, 'B=',B)
        (a,b), (c,d) = A.split(','), B.split
        #(a,b) = input().split(',')
        #(c,d) = input().split(',')
        v1.append((float(a), float(b)))
        v2.append((float(c), float(d)))
        n+=1
    print('invalid data')

'''