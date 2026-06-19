class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        rows = [''] * numRows
        currentRow = 0
        direction = 1
        
        for char in s:
            rows[currentRow] += char
            if currentRow == 0:
                direction = 1
            elif currentRow == numRows - 1:
                direction = -1
            currentRow += direction

        return ''.join(rows)