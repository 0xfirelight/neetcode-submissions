# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:

        self.qs(pairs, 0, len(pairs)-1)
        return pairs


    def qs(self, pairs: List[Pair], lo: int, hi: int):
        if lo < hi:
            idx = self.partition(pairs, lo, hi)

            self.qs(pairs, lo, idx-1)
            self.qs(pairs, idx+1, hi)

    def partition(self, pairs: List[Pair], lo: int, hi: int) -> int:

        pivot = pairs[hi]
        idx = lo -1

        for i in range(lo, hi):
            if pairs[i].key < pivot.key:
                idx += 1
                pairs[i], pairs[idx] = pairs[idx], pairs[i]

        idx += 1
        pairs[hi] = pairs[idx]
        pairs[idx] = pivot

        return idx

        