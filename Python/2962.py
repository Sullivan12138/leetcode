class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        q = 0
        start = 0
        start2 = 0
        n = len(nums)
        max = 0
        max_num = 0
        sum = 0
        while q < n:
            if nums[q] > max:
                max = nums[q]
            q += 1
        q = 0
        x = []
        while q < n:
            if nums[q] == max:
                max_num += 1
                x.append(q)
            if max_num >= k:
                sum += x[max_num - k] + 1
            q += 1
        return sum


