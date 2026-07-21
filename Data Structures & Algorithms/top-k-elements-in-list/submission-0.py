class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        answer = sorted(count.items(), key=lambda val: val[1], reverse=True)[:k]
        return [x for x, _ in answer]

        