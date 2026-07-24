class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [0] * len(nums)
        prefixes[0] = 1
        for i in range(1, len(nums)):
            prefixes[i] = nums[i-1] * prefixes[i-1]

        suffixes = [0] * len(nums)
        suffixes[len(nums)-1] = 1
        for i in range(len(nums) - 2, -1, -1):
            suffixes[i] = nums[i+1] * suffixes[i+1]

        results = []
        for i in range(len(nums)):
            results.append(prefixes[i] * suffixes[i]) 

        return results
        