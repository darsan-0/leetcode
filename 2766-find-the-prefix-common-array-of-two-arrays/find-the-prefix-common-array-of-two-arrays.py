class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        C =[]
        
        for i in range (0,len(A)): 
            count = 0

            for j in range (0,i+1):
                if A[j] in B[:i+1]:
                    count += 1

            C.append(count)
            
        return C 
