class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x != 0 and x % 10 == 0:
            return False
        
        rev = 0
        num = x
        while num > rev:
            rev = rev * 10 + (num % 10)
            num //= 10
        return num == rev or num == rev // 10


        