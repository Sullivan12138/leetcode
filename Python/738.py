class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        def isIncreasing(l):
            for i in range(len(l) - 1, 0, -1):
                if l[i-1] > l[i]:
                    return i
            return 0
        if N < 10:
            return N
        l = [int(item) for item in str(N)]
        while True:
            i = isIncreasing(l)
            if i == 0:
                break
            l[i-1] -= 1
            for j in range(i, len(l)):
                l[j] = 9
        sum = 0
        for i in range(0, len(l)):
            sum += (10 ** (len(l) - 1 - i)) * l[i]
        return sum 