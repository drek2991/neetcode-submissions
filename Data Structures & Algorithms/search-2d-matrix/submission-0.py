class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(arr: List[int]) -> bool:
            l = 0
            r = len(arr)
            while l < r:
                mid = (l + r) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target: 
                    l = mid + 1
                else:
                    r = mid
            return False
        
        left = 0
        right = len(matrix)
        while left < right:
            middle = (left + right) // 2
            if target >= matrix[middle][0] and target <= matrix[middle][-1]:
                return search(matrix[middle])
            elif target < matrix[middle][0]:
                right = middle
            else:
                left = middle + 1
        return False