class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Negative numbers are not palindromes
        if x < 0:
            return False

        original = x
        res = 0

        while x != 0:
            rem = x % 10
            res = res * 10 + rem
            x //= 10

        if original == res:
            return True
        else:
            return False
