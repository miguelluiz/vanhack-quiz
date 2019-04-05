# vanhack-quiz-A
SOFTWARE DEVELOPER - TECHNICAL TEST - Question A

Your goal for this question is to write a program that accepts 
two lines (x1,x2) and (x3,x4) on the x-axis 
and returns whether they overlap. 

As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).

The solution was based on the following schema:

                 A0------------------A1
      B0------B1                          B0------B1
      
          if B1<A0 OR B0>A1 then
             Line B does NOT overlap Line A
          else
             Line B DOES ovelap Line A


Therefore, we need to make sure the A and B are ordered:

    def swap(X):
        '''
        this function does make sure the pair is 
        ordered (a,b) where a<b
        (10, -5) would become (-5, 10)
        '''
        if X[0]>X[1]:
            return (X[1],X[0])
        return X
      
    A, B = swap(A), swap(B)
    
 Proposed solution:
 
 def isOverlapR2(A,B):
 
    # Return True if A Line overlaps B Line; False otherwise
    
    A, B = swap(A), swap(B)
    
    return not (B[1]<A[0] or B[0]>A[1])

In order to call this function, please take a look at the testOverlapV0.py

(venv) C:\work\vanhack\venv\Quiz\test_A>python testOverlapV0.py

This program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns 
whether they overlap (True) or not overlap (False)

Enter total number of lines to check, default=1 pair to check

please add  1 lines to be checked - use comma

(1,2),(3,4) should be typed as 1,2,3,4

1,5,2,6

(1.0, 5.0) (2.0, 6.0) True

True means (1,2) and (5,6) do overlap

Let's check the following pair (1,5) and (6,8)

(1,5) and (6,8) should be entered as below:

1,5,6,8


(1.0, 5.0) (6.0, 8.0) False

False means (1,2) and (6,8) do NOT overlap

Note:
 We are using float although has no mention about it - set/intersection could also handle it but only for int figures
 
 in order to run it as a batch module, a text file should be created with n pairs (comma separeted) as follow:
 
 first line, number of pair to check
 second line next pair to check
 and so on
 
ex:
 
4

13 , -6 , -8 , 3

-15 , -6 , 4 , -11

-4 , -2 , 0 , -20

-18 , 9 , 10 , 12

** please check testample.txt ** 

(venv) C:\work\vanhack\venv\Quiz\test_A>python testOverlapV0.py <testsample.txt

This program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap
Enter total number of lines to check, default=1 pair to check
please add  100 lines to be checked - use comma
(1,2),(3,4) should be typed as 1,2,3,4

(13.0, -6.0) (-8.0, 3.0) True

(-15.0, -6.0) (4.0, -11.0) True

(-4.0, -2.0) (0.0, -20.0) True

(-18.0, 9.0) (10.0, 12.0) False






