# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self.msort(pairs, 0, len(pairs))
        return pairs

    def msort(self, pairs: List[Pair], start: int, end: int):
        if end - start <= 1:
            return

        mid = start + (end - start) // 2
        # sort left
        self.msort(pairs, start, mid)
        # sort right
        self.msort(pairs, mid, end)
        
        # merge them together
        left = pairs[start:mid]
        right = pairs[mid:end]

        lp = 0
        rp = 0
        i = start

        # compare each left and right element and use the one that's smaller first
        while i < len(pairs) and lp < len(left) and rp < len(right):
            if left[lp].key <= right[rp].key:
                pairs[i] = left[lp]
                lp += 1
            else:
                pairs[i] = right[rp]
                rp += 1
            i += 1

        # add remaining elements
        while lp < len(left):
            pairs[i] = left[lp]
            lp += 1
            i += 1

        while rp < len(right):
            pairs[i] = right[rp]
            rp += 1
            i += 1
