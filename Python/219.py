class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0:
            return False
        n = len(nums)
        d = {}
        for i, num in enumerate(nums):
            if num in d and (i - d[num]) <= k:
                return True
            d[num] = i
        return False