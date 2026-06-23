class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        if not s:
            return 0
        
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        result = 0
        for c in s:
            if not c.isdigit():
                break
            result = result * 10 + int(c)

        result *= sign
        return max(-2**31, min(2**31 - 1, result))
        