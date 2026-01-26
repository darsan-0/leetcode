class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        calt = 0
        max_alt =0
        for i in gain:
            calt += i
            if calt > max_alt:
                max_alt = calt
        return max_alt

        