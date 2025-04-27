class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        MAX_LEN = len(s)
        MAX_ROW = numRows+1
        m = [[""] * MAX_LEN for _ in range(MAX_ROW)]
        if numRows == 1:
            return s
        if numRows == 2:
            for i in range(len(s)):
                row = i % 2
                col = i // 2
                m[row][col] = s[i]
        else:     
            T = numRows * 2 - 2
            for i in range(len(s)):
                x = i % T 
                y = i // T
                if x < numRows:
                    col = y * 2
                    row = x
                else:
                    col = y * 2 + 1
                    row = numRows -1 - (x-numRows+1)
                m[row][col] = s[i]
        str = ""
        for i in range(MAX_ROW):
            for j in range(MAX_LEN):
                str += m[i][j]
        return str