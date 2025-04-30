def merge(intervals):
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


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        n = len(intervals)
        if newInterval[0] < intervals[0][0]:
            for j in range(n - 1, 0, -1):
                intervals[j] = intervals[j - 1]
            intervals[0] = newInterval
        else:
            for i in range(n - 1):
                if intervals[i][0] <= newInterval[0] and intervals[i + 1][0] > newInterval[0]:

                    for j in range(n - 1, i, -1):
                        intervals[j] = intervals[j - 1]
                    intervals[i + 1] = newInterval
                    break
        print(intervals)
        return merge(intervals)