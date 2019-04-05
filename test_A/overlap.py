#https://github.com/miguelluiz/vanhack-quiz-A/blob/master/README.md
import sys
def isOverlapR2(A,B):
    '''
    Return True if A Line overlaps B Line; False otherwise
    '''
    if sys.version.split(' ')[0]<'3':
        print ('Python 3 is required')
        exit()
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
    '''
                  A0------------------A1
      B0------B1                          B0------B1
          if B1<A0 OR B0>A1 then
             Line B does NOT overlap Line A
          else
             Line B DOES ovelap Line A
    '''
    return not (B[1]<A[0] or B[0]>A[1])