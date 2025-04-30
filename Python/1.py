class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        m = collections.defaultdict(int)
        for i in range(n):
            if target - nums[i] in m.keys():
                return [m[target-nums[i]], i]
            else:
                m[nums[i]] = i