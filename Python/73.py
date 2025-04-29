class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        idx = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    idx.append((i,j))
        for t in range(len(idx)):
            i, j = idx[t]
            for k in range(m):
                matrix[k][j] = 0
            for k in range(n):
                matrix[i][k] = 0
        return matrix