# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.qsort(pairs, 0, len(pairs))
        return pairs
    

    def qsort(self, pairs: List[Pair], s: int, e: int):
        if e - s <= 1:
            return 

        pivot = pairs[e-1]
        left = s

        for i in range(s, e):
            if pairs[i].key < pivot.key:
                pairs[left], pairs[i] = pairs[i], pairs[left]
                left += 1
            

        pairs[e-1] = pairs[left]
        pairs[left] = pivot

        self.qsort(pairs, s, left)
        self.qsort(pairs, left+1, e)
        