class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        a, b, c, d = 1001, 1001, 1001, 1001
        n = len(matrix)
        x = n // 2
        for i in range(x):
            for j in range(x):
                a = matrix[i][j]
                b = matrix[j][n - 1 - i]
                c = matrix[n - 1 - i][n - 1 - j]
                d = matrix[n - 1 - j][i]
                matrix[i][j] = d
                matrix[j][n - 1 - i] = a
                matrix[n - 1 - i][n - 1 - j] = b
                matrix[n - 1 - j][i] = c
        if n % 2 == 1:
            j = n // 2
            for i in range(n // 2):
                a = matrix[i][j]
                b = matrix[j][n - 1 - i]
                c = matrix[n - 1 - i][n - 1 - j]
                d = matrix[n - 1 - j][i]
                matrix[i][j] = d
                matrix[j][n - 1 - i] = a
                matrix[n - 1 - i][n - 1 - j] = b
                matrix[n - 1 - j][i] = c
        return matrix



