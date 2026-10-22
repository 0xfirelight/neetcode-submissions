class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cache = {}

        for n in nums:
            cache[n] = True

        longest = 0
        for n in nums:
            if not cache.get(n-1):
                length = 1
                while (n + length) in cache:
                    length += 1

                longest = max(longest, length)



        return longest


        