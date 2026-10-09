class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        freqs = [[] for i in range(len(nums) + 1)]

        for n in nums:
            counter[n] = 1 + counter.get(n, 0)

        for (num, cnt) in counter.items():
            freqs[cnt].append(num)

        res = []
        for i in range(len(freqs)-1, 0, -1):
            for num in freqs[i]:
                res.append(num)
                if len(res) == k:
                    return res




        

        