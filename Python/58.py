class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        num = 0
        flag = True
        idx = 0
        for i in range(n):
            if s[i] == ' ':
                flag = True
            else:
                if flag:
                    flag = False
                    num = 0
                num += 1
        return num