class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        p = 0
        q = 0
        res = 0
        flag = False
        while p < m:
            if haystack[p] == needle[q]:
                if not flag:
                    res = p
                    flag = True
                q += 1
            else:
                if flag:
                    p = res
                    flag = False
                q = 0
            if q == n:
                return res
            p += 1
        return -1

        