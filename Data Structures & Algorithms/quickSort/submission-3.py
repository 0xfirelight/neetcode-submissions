# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.qsort(pairs, 0, len(pairs) - 1)
        return pairs


    def qsort(self, pairs: List[Pair], lo: int, hi: int):
        if len(pairs) <= 1:
            return pairs

        if lo >= hi:
            return

        p = self.partition(pairs, lo, hi)

        self.qsort(pairs, lo, p-1)
        self.qsort(pairs, p+1, hi)
        

    def partition(self, pairs: List[Pair], lo: int, hi: int) -> int:
        p = pairs[hi]
        lp = lo
        for i in range(lo, hi):
            if pairs[i].key < p.key:
                pairs[i], pairs[lp] = pairs[lp], pairs[i]
                lp += 1

        pairs[hi] = pairs[lp]
        pairs[lp] = p

        return lp 
        