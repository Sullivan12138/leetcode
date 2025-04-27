class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 0
        q = 1
        r = 2
        n = len(nums)
        while r < n:
            if nums[p] != nums[q]:
                nums[q+1] = nums[r]
                p += 1
                q += 1
                r += 1
            else:
                if nums[r] == nums[q]:
                    r += 1
                else:
                    nums[q+1] = nums[r]
                    p += 1
                    q += 1
                    r += 1
        q += 1
        return q