class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = {}
        n = len(nums)
        p = 0
        q = 1
        while q < n:
            if nums[p] == nums[q]:
                q += 1
            else:
                nums[p+1] = nums[q]
                p += 1
                q += 1
        return p+1