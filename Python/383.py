class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        m = len(ransomNote)
        n = len(magazine)
        d = {}
        for i in range(n):
            if magazine[i] not in d.keys():
                d[magazine[i]] = 1
            else:
                d[magazine[i]] += 1
        for i in range(m):
            if ransomNote[i] not in d.keys() or d[ransomNote[i]] == 0:
                return False
            else:
                d[ransomNote[i]] -= 1
        return True