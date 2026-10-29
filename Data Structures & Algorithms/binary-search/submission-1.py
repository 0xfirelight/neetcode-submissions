class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        start = 0
        end = n

        while start < end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                end = mid
            else:
                start = mid + 1

        return -1
            
        