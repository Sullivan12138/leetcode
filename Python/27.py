class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        k = 0
        for i in range(n):
            if nums[i] == val:
                nums[i] = 51
            else:
                k += 1
        nums.sort()
        return k
            