# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self.sort_in_place(pairs, 0, len(pairs))
        return pairs

    def sort_in_place(self, arr: List[Pair], start: int, end: int):
        if (end - start) + 1 <= 1:
            return

        pivot = (start + end) // 2
        # left
        self.sort_in_place(arr, start, pivot)
        # right
        self.sort_in_place(arr, pivot + 1, end)

        L = arr[start: pivot + 1]
        R = arr[pivot + 1: end + 1]

        l = 0
        r = 0
        i = start

        while l < len(L) and r < len(R):
            if L[l].key <= R[r].key:
                arr[i] = L[l]
                l+=1
            else:
                arr[i] = R[r]
                r+=1
            i += 1

        while l < len(L):
            arr[i] = L[l]
            i += 1
            l += 1

        while r < len(R):
            arr[i] = R[r]
            i += 1
            r += 1

