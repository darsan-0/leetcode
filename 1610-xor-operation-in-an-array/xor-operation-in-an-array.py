class Solution(object):
    def xorOperation(self, n, start):
        nums = []
        for i in range(0,n):
            nums.append(start + 2 * i)
        result =0
        for i in nums:
            result ^= i 
        return result
        