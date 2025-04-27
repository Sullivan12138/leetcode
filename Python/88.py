class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return 
        nums3 = []
        p = 0
        q = 0
        while p < m and q < n:
            if nums1[p] < nums2[q]:
                nums3.append(nums1[p])
                p+=1
            elif nums1[p] > nums2[q]:
                nums3.append(nums2[q])
                q+=1
            else:
                nums3.append(nums1[p])
                nums3.append(nums2[q])
                p += 1
                q += 1
        if q < n:
            for i in range(q, n):
                nums3.append(nums2[i])
        if p < m:
            for i in range(p, m):
                nums3.append(nums1[i])
        for i in range(m+n):
            nums1[i] = nums3[i]
        return
        