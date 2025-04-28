class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        p = 1
        q = n
        while p < q:
            if numbers[p-1] + numbers[q-1] == target:
                return [p, q]
            elif numbers[p-1] + numbers[q-1] > target:
                q -= 1
            else:
                p += 1
