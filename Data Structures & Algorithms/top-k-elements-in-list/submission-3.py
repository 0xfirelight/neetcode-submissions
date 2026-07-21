class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        results = []
        num_to_count = {}
        arr = []

        # find most frequent element
        # check if it's already in the results
        for n in nums:
            num_to_count[n] = 1 + num_to_count.get(n, 0)

        for n, v in num_to_count.items():
            arr.append([v, n])

        arr.sort()

        res = []
        while len(res) < k:
            print(len(res))
            print(k)
            res.append(arr.pop()[1])

        print(res)
        return res 

        

        