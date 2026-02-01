class Solution(object):
    def plusOne(self, digits):
        
        digits1 = [str(i) for i in digits]
        res = ''.join(digits1)
        sum = int(res)+1


        output = [int(i) for i in str(sum)]

        return output