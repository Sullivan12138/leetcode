class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        m = 1
        for i in range(1,min(n,k)+1):
            if n % i == 0 and k % i == 0:
                m = i
        if k == 0:
            return
        for j in range(m):
            idx = j
            tmp = nums[j]
            tmp2 = nums[j]
            i = (idx + k) % n
            while True:
                tmp2 = nums[i]
                nums[i] = tmp
                tmp = tmp2
                idx = i
                i = (idx + k) % n
                if idx == j:
                    break

        