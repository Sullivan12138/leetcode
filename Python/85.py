class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        left = [[0 for _ in range(n)] for _ in range(m)]
        minWidth = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    left[i][j] = 0
                elif j == 0:
                    left[i][j] = 1
                else:
                    left[i][j] = left[i][j-1] + 1
        maxArea = 0
        for i in range(m):
            for j in range(n):
                maxAreaJ = 0
                for k in range(i, -1, -1):
                    width = left[k][j]
                    if k == i:
                        minWidth[k][j] = left[k][j]
                    else:
                        minWidth[k][j] = min(left[k][j], minWidth[k+1][j])
                    area = minWidth[k][j] * (i+1-k)
                    if area > maxAreaJ:
                        maxAreaJ = area 
                if maxAreaJ > maxArea:
                    maxArea = maxAreaJ
        return maxArea