# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.sortRec(pairs)

    def sortRec(self, pairs: List[Pair]) -> List[Pair]:
        # base case
        if len(pairs) <= 1:
            return pairs

        pivot = len(pairs) // 2
        left = self.sortRec(pairs[:pivot])
        right = self.sortRec(pairs[pivot:])

        l = 0
        r = 0
        i = 0

        while l < len(left) and r < len(right):
            if left[l].key <= right[r].key:
                pairs[i] = left[l]
                l+=1
            else:
                pairs[i] = right[r]
                r+=1
            i += 1

        while l < len(left):
            pairs[i] = left[l]
            i += 1
            l += 1

        while r < len(right):
            pairs[i] = right[r]
            i += 1
            r += 1
        
        return pairs


