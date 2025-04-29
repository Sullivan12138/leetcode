class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])
        m2 = [[False] * n for _ in range(m)]
        direction = [0,1,2,3]
        res = []
        i = 0
        j = 0
        d = 0
        while True:
            res.append(matrix[i][j])
            m2[i][j] = True
            if d == 0:
                if j == n - 1 or m2[i][j+1] == True:
                    d = 1
                    if i == m-1 or m2[i+1][j] == True:
                        return res
                    i += 1
                else:
                    j += 1
            elif d == 1:
                if i == m-1 or m2[i+1][j] == True:
                    d = 2
                    if j == 0 or m2[i][j-1] == True:
                        return res
                    j -= 1
                else:
                    i += 1
            elif d == 2:
                if j == 0 or m2[i][j-1] == True:
                    d = 3
                    if i == 0 or m2[i-1][j] == True:
                        return res
                    i -= 1
                else:
                    j -= 1
            elif d == 3:
                if i == 0 or m2[i-1][j] == True:
                    d = 0
                    if j == n - 1 or m2[i][j+1] == True:
                        return res
                    j += 1
                else:
                    i -= 1
            else:
                pass