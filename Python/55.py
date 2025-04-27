class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        idx = 0
        p = 0
        q = 0
        i = 0
        can_skip = False
        while idx < n:
            if nums[idx] == 0:
                q = p
                p = idx
                i = q
                max = 0
                while i < p:
                    if nums[i] > p-i:
                        can_skip = True
                        if nums[i] + i > max:
                            max = nums[i] + i
                    i += 1
                idx = max
                if idx >= n-1:
                    return True
                if can_skip is False:
                    return False
                can_skip = False 
            else:
                idx += 1
            if idx == n-1:
                return True
            i = 0
        return True
                
            

