class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        freqs = [[] for i in range(len(nums) + 1)]

        for n in nums:
            counter[n] = 1 + counter.get(n, 0)

        for n, cnt in counter.items():
            freqs[cnt].append(n)

        res = []
        for i in range(len(freqs)-1, 0, -1):
            for n in freqs[i]:
                res.append(n)
                if len(res) == k:
                    return res




        