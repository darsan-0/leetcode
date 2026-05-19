class Solution(object):
    def merge(self, nums1, m, nums2, n):

        output = []

        for i in range(m):
            output.append(nums1[i])

        for i in range(n):
            output.append(nums2[i])

        output.sort()

        for i in range(m + n):
            nums1[i] = output[i]