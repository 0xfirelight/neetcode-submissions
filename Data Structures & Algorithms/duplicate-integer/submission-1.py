class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for i in range(len(nums)):
            if not counter.get(nums[i]):
                counter[nums[i]] = 1
            else: 
                return True
        return False