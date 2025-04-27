class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        m = len(set(nums))
        n = len(nums)
        right = 0
        cnt = {}
        res = 0
        for left in range(n):
            while right < n and len(cnt) < m:
                if nums[right] in cnt.keys():
                    cnt[nums[right]] += 1
                else:
                    cnt[nums[right]] = 1
                right += 1
            if len(cnt) == m:
                res += n - right + 1
            cnt[nums[left]] -= 1
            if cnt[nums[left]] == 0:
                cnt.pop(nums[left])
        return res
        