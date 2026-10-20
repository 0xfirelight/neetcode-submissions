class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        res = [0] * (m + n)
        l, r, i = 0, 0, 0
        
        while l < m and r < n:
            if nums1[l] <= nums2[r]:
                res[i] = nums1[l]
                l += 1
            else:
                res[i] = nums2[r]
                r += 1
            i += 1

        while l < m:
            res[i] = nums1[l]
            l += 1
            i += 1

        while r < n:
            res[i] = nums2[r]
            r += 1
            i += 1

        for j in range(n+m):
            nums1[j] = res[j]
        