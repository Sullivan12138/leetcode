class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p = 0
        q = 0
        n = len(s)
        m = len(t)
        while p < n and q < m:
            if s[p] == t[q]:
                p += 1
            q += 1
        if p == n:
            return True
        return False