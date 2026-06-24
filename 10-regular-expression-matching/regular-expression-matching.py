class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = True

        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    zero_occurrences = dp[i][j - 2]
                    one_or_more = (p[j - 2] == '.' or s[i - 1] == p[j - 2]) and dp[i - 1][j]
                    dp[i][j] = zero_occurrences or one_or_more
                elif p[j - 1] == '.' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]