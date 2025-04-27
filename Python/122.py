class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        q = 0
        n = len(prices)
        max = 0
        while p < (n-1):
            if prices[p+1] < prices[p]:
                p += 1 
            q = p
            while q < (n-1) and prices[q+1] > prices[q]:
                q += 1
            max += prices[q] - prices[p]
            p = q+1
        return max