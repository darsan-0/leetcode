class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        actual_sum = sum(nums)
        n = len(nums)
        Total_nums = int(n*(n+1)/2)
        return Total_nums - actual_sum