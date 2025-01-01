class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            mid_row = (top + bottom) // 2
            if matrix[mid_row][0] > target:
                bottom = mid_row-1
            elif matrix[mid_row][-1] < target:
                top = mid_row+1
            else:
                break
        
        if top > bottom:
            return False

        l = 0
        r = len(matrix[0]) - 1

        while l<=r:
            mid_col = (l+r)//2
            if matrix[mid_row][mid_col] > target:
                r = mid_col-1
            elif matrix[mid_row][mid_col] < target:
                l = mid_col+1
            else:
                return True
        
        return False
