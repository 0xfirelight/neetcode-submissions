# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self.sort(pairs, 0, len(pairs))
        return pairs


    def sort(self, pairs: List[Pair], start: int, end: int):
        if end - start <= 1:
            return

        mid = (start + end) // 2

        # sort left
        self.sort(pairs, start, mid)
        # sort right
        self.sort(pairs, mid, end)

        # merge
        left = pairs[start:mid]
        right = pairs[mid:end]

        l = 0
        r = 0
        i = start

        while i < end and l < len(left) and r < len(right):
            if left[l].key <= right[r].key:
                pairs[i] = left[l]
                l += 1
            else: 
                pairs[i] = right[r]
                r += 1
            i += 1

        while l < len(left):
            pairs[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            pairs[i] = right[r]
            r += 1
            i += 1







