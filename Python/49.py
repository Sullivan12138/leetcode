class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        m = collections.defaultdict(list)
        for word in strs:
            cnt = [0] * 26
            for c in word:
                cnt[ord(c)-ord('a')] += 1
            m[tuple(cnt)].append(word)
        return list(m.values())