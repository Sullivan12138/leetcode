class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        sum = [0] * (n+1)
        sum[0] = 0
        sum[1] = 0
        for i in range(2, n+1):
            sum[i] = min(sum[i-1] + cost[i-1], sum[i-2] + cost[i-2])
        return sum[n]
        # 另解
        # prev = curr = 0
        # for i in range(1, n):
        #     nxt = min(prev + cost[i-1], curr + cost[i])
        #     prev, curr = curr, nxt
        # return curr