class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = len(s)
        n = len(t)
        d = {}
        if m != n:
            return False
        for i in range(m):
            if s[i] not in d.keys():
                d[s[i]] = 1
            else:
                d[s[i]] += 1
        for i in range(n):
            if t[i] not in d.keys() or d[t[i]] == 0:
                return False
            else:
                d[t[i]] -= 1
        return True
