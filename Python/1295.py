def cal(n):
    res = 0
    while n >= 10:
        n = n // 10
        res += 1
    res += 1
    return (res % 2 == 0)
class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            if cal(num):
                res += 1
        return res