class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(n):
            gas[i] = gas[i] - cost[i]
        res = 0
        i = 0
        sum = 0
        while i < 2*n:
            sum += gas[i%n]
            if sum < 0:
                sum = 0
                res = (i+1)%n
            else:
                if i - res == n-1:
                    return res
            i += 1
        return -1