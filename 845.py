class Solution:
    def longestMountain(self, A):
        n = len(A)
        if n == 0:
            return 0
        left = [0] * n
        right = [0] * n
        mountainLength = [0] * n 
        for i in range(1, n):
            if A[i] > A[i-1]:
                left[i] = left[i-1] + 1
            else:
                left[i] = 0
        for i in range(n - 2, -1, -1):
            if A[i] > A[i+1]:
                right[i] = right[i+1] + 1
            else:
                right[i] = 0
        for i in range(1, n - 1):
            if left[i] == 0 or right[i] == 0:
                continue
            mountainLength[i] = left[i] + right[i] + 1
        return max(mountainLength)


s = Solution()
print(s.longestMountain([0,1,4,7,3,2,1,5]))