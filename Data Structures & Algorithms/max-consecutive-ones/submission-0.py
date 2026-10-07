class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_n = 0
        counter = 0
        for n in nums:
            if n == 1:
                counter += 1
                max_n = max(max_n, counter)
            else:
                counter = 0
        return max_n
        