class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if nums == []:
            return []
        start = nums[0]
        end = nums[0]
        res = []
        res2 = []
        for i, num in enumerate(nums):
            end = nums[i]
            if i < len(nums) - 1:
                if nums[i+1] != nums[i] + 1:
                    res.append((start, end))
                    start = nums[i + 1]
            else:
                res.append((start, end))
        for (i, j) in res:
            if i == j:
                res2.append(str(i))
            else:
                s = str(i)
                s += "->"
                s += str(j)
                res2.append(s)
        return res2