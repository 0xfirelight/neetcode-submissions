class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.bsMatrix(matrix, target)
    
    def bsMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        start = 0
        end = n

        while start < end:
            mid = start + (end - start) // 2

            print(matrix[mid][0])

            if target == matrix[mid][0]:
                return True

            if target > matrix[mid][0]:
                if (mid + 1) < n:
                    if target < matrix[mid+1][0]:
                        return self.bs(matrix[mid], target)
                elif self.bs(matrix[mid], target):
                    return True

                start = mid + 1

            if target < matrix[mid][0]:
                if (mid - 1) >= 0:
                    if target > matrix[mid][0]:
                        return self.bs(matrix[mid], target)
                elif self.bs(matrix[mid], target):
                    return True

                end = mid

        return False
        
    
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
                
    
        