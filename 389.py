class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s2 = sorted(s)
        t2 = sorted(t)
        p = 0
        while p < len(s2):
            if s2[p] != t2[p]:
                return t2[p]
            p += 1
        return t2[p]