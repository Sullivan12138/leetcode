def cmp(a, b):
    if a[0] > b[0]:
        return 1
    if a[0] < b[0]:
        return -1
    return 0
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=functools.cmp_to_key(cmp))
        print(intervals)
        max_end = intervals[0][1]
        start = intervals[0][0]
        res = []
        for interval in intervals[1:]:
            if interval[0] > max_end:
                res.append([start, max_end])
                start = interval[0]
            max_end = max(max_end, interval[1])
        res.append([start, max_end])
        return res