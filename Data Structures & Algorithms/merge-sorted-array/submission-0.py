class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        j = 0
        for i in range(m, n + m):
            nums1[i] = nums2[j]
            j += 1

        ers = self.merge_sort(nums1, 0, n + m)
            

    def merge_sort(self, arr: List[int], start, end):
        if end - start <= 1:
            return arr

        mid = (end + start) // 2

        self.merge_sort(arr, start, mid)
        self.merge_sort(arr, mid, end)

        left = arr[start:mid]
        right = arr[mid:end]

        l = 0
        r = 0
        i = start

        res = [] * len(arr)
        while l < len(left) and r < len(right) :
            if left[l] <= right[r]:
                arr[i] = left[l]
                l += 1
            else:
                arr[i] = right[r]
                r += 1
            i += 1

        while l < len(left):
                arr[i] = left[l]
                l += 1
                i += 1

        while r < len(right):
                arr[i] = right[r]
                r += 1
                i += 1



        