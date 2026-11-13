# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.qs(pairs, 0, len(pairs) - 1)
        return pairs

    def qs(self, pairs: List[Pair], start: int, end: int):
        if end - start + 1 <= 1:
            return

        p = self.partition(pairs, start, end)

        self.qs(pairs, start, p - 1)
        self.qs(pairs, p + 1, end)


    def partition(self, pairs: List[Pair], start: int, end: int) -> int:
        pivot = end
        lp = start

        for i in range(start, end+1):
            if pairs[i].key < pairs[pivot].key:
                pairs[lp], pairs[i] = pairs[i], pairs[lp]
                lp += 1
        
        pairs[lp], pairs[pivot] = pairs[pivot], pairs[lp]
        return lp



        