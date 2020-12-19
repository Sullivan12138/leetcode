class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        b = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                b[j][n-1-i] = matrix[i][j]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = b[i][j]