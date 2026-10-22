class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)

        while start < end:
            pivot = (start + end) // 2
            if target == nums[pivot]:
                return pivot
            if target < nums[pivot]:
                end = pivot
                continue
            start = pivot + 1
        
        return -1
        