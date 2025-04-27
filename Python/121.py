class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max = 0
        min = 10 ** 4 + 5
        for i in range(n):
            if prices[i] < min:
                min = prices[i]
            if prices[i] - min > max:
                max = prices[i] - min
        return max
        