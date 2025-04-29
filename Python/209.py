class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        p = 0
        sum = 0
        x = 0
        res = 10**5 + 5
        for i in range(n):
            sum += nums[i]
            x += 1
            if sum >= target:
                while True:
                    if p == i or (sum - nums[p]) < target:
                        if x < res:
                            res = x
                        break
                    sum -= nums[p]
                    x -= 1
                    p += 1
        if sum < target:
            return 0
        return res