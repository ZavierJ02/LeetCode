class Solution(object):
    def romanToInt(self, s):
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        n = len(s)

        for i in range(n):
            current = values[s[i]]

            if i + 1 < n:
                next = values[s[i + 1]]
            else:
                next = 0
            
            if current < next:
                total -= current
            else:
                total += current

        return total