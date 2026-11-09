# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self.msort(pairs, 0, len(pairs))
        return pairs
    

    def msort(self, pairs: List[Pair], lo: int, hi: int) -> List[Pair]:
        if hi - lo <= 1:
            return

        mid = lo + (hi - lo) // 2
        
        self.msort(pairs, lo, mid)
        self.msort(pairs, mid, hi)

        left = pairs[lo:mid]
        right = pairs[mid:hi]

        lp = 0
        rp = 0
        i = lo

        while i < len(pairs) and lp < len(left) and rp < len(right):
            if left[lp].key <= right[rp].key:
                pairs[i] = left[lp]
                lp += 1
            else:
                pairs[i] = right[rp]
                rp += 1
            i += 1

        while lp < len(left):
            pairs[i] = left[lp]
            lp += 1
            i += 1

        while rp < len(right):
            pairs[i] = right[rp]
            rp += 1
            i += 1


        



