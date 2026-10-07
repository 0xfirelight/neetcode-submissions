class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1] * len(arr)
        n = len(arr)

        current_max = -1
        for i in range(n-1, -1, -1):
            res[i] = current_max
            current_max = max(current_max, arr[i])
        return res
                

        