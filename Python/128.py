class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        l = 0
        res = 0
        max_num = 0
        d = {}
        for num in nums:
            if l == 0 or num == max_num + 1:
                if l == 0:
                    l = 1
                else:
                    l += 1
            else:
                if num not in d:
                    l = 1
            max_num = num
            d[num] = 1
            if l > res:
                res = l
        return res