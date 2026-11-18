class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        s = numbers[r] + numbers[l]
        while s != target and l < r:
            if s > target:
                r -= 1
            else: 
                l += 1
            s = numbers[r] + numbers[l]

        return [l + 1, r + 1]
