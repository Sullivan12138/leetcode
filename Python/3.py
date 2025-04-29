class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        n = len(s)
        p = 0
        sum = 0
        res = 0
        for i in range(n):
            sum += 1
            if s[i] not in d.keys():
                d[s[i]] = 1
                if sum > res:
                    res = sum
            else:
                d[s[i]] += 1
                while p <= i and d[s[i]] > 1:
                    d[s[p]] -= 1
                    if d[s[p]] == 0:
                        d.pop(s[p])
                    p += 1
                    sum -= 1
        return res
