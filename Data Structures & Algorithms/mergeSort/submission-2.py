# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self.sort(pairs, 0, len(pairs))
        return pairs
    

    def sort(self, arr: List[Pair], start: int, end: int):
        if end - start <= 1:
            return

        mid = (start + end) // 2
        self.sort(arr, start, mid)
        self.sort(arr, mid, end)

        # merge
        left = arr[start:mid]
        right = arr[mid: end]

        i = start
        l = 0
        r = 0

        while l < len(left) and r < len(right):
            if left[l].key <= right[r].key:
                arr[i] = left[l]
                l += 1
            else:
                arr[i] = right[r]
                r += 1
            i += 1

        while l < len(left):
            arr[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            arr[i] = right[r]
            r += 1
            i += 1




