class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.bsMatrix(matrix, target)
    
    def bsMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start, end = 0, len(matrix) - 1
        while start <= end:
            mid = (start + end) // 2

            if matrix[mid][0] <= target:
                start = mid + 1
            else:
                end = mid - 1
        
        return self.bs(matrix[end], target)

        
    
    def bs(self, arr: list[int], target: int) -> bool:
        n = len(arr)
        start = 0
        end = n

        while start < end:
            mid = start + (end - start) // 2

            if target < arr[mid]:
                end = mid
            elif target > arr[mid]:
                start = mid + 1
            else:
                return True
        
        return False
                
    
        