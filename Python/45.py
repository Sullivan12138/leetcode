class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = [0] * n
        for i in range(n):
            cnt[i] = i
        i = 0
        while i < n:
            for j in range(i+1, min(n, i+nums[i]+1)):
                if cnt[j] > cnt[i]+1:
                    cnt[j] = cnt[i] + 1
                if j == n-1:
                    return cnt[n-1]
            i += 1
        return cnt[n-1]
