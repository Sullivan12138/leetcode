class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p = list(pattern)
        s2 = s.split()
        d = collections.defaultdict(list)
        d2 = collections.defaultdict(list)
        i = j = 0
        while i < len(p) and j < len(s2):
            if p[i] in d and d[p[i]] != s2[j]:
                return False
            elif p[i] not in d:
                d[p[i]] = s2[j]
            if s2[j] in d2 and d2[s2[j]] != p[i]:
                return False
            elif s2[j] not in d2:
                d2[s2[j]] = p[i]
            i += 1
            j += 1
        if i < len(p) or j < len(s2):
            return False
        return True