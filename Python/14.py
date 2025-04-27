class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        i = 0
        m = len(strs[0])
        flag = True
        while i < m:
            x = strs[0][i]
            for j in range(n):
                if i >= len(strs[j]):
                    flag = False
                    break
                if strs[j][i] != x:
                    flag = False
                    break
            if not flag:
                break
            i += 1
        if i == 0:
            return ""
        else:
            return strs[0][:i]