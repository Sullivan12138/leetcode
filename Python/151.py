class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        words = []
        flag = True
        word = ""
        for i in range(n):
            if s[i] == ' ':
                if not flag:
                    flag = True
                    words.append(word)
            else:
                if flag:
                    flag = False
                    word = ""
                word += s[i]
        if not flag:
            words.append(word)
        m = len(words)
        res = ""
        words = list(reversed(words))
        for i in range(m):
            res += words[i]
            if i != m-1:
                res += " "
        return res
