class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ""
        n = len(s)
        for i in range(n):
            if s[i] >= '0' and s[i] <= '9':
                s2 += (s[i])
            elif s[i] >= 'a' and s[i] <= 'z':
                s2 += (s[i])
            elif s[i] >= 'A' and s[i] <= 'Z':
                s2 += (s[i].lower())
        p = 0
        q = len(s2)-1
        flag = True
        while p < q:
            if s2[p] != s2[q]:
                return False
            p += 1
            q -= 1
        return True