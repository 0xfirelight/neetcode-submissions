class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = {}
        for i in range(len(nums)):
            counter[nums[i]] = i
        for i in range(len(nums)):
            pair_idx = counter.get(target - nums[i]) 
            if pair_idx == i: 
                continue
            if pair_idx:
                if i > pair_idx:
                    return [pair_idx, i]
                else:
                    return [i, pair_idx]
        return None
