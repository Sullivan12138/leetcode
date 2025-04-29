class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            p = i+1
            q = n-1
            while p < q:
                if nums[p] + nums[q] == -nums[i]:
                    res.append([nums[i], nums[p], nums[q]])
                    p += 1
                    q -= 1
                elif nums[p] + nums[q] > -nums[i]:
                    q -= 1
                else:
                    p += 1
        res=list(set([tuple(t) for t in res]))
        return res