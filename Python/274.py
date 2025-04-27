class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        h = min(n, citations[n-1])
        i = 1
        while i < h+1:
            if citations[n-i] < i:
                break
            i += 1
        return i-1