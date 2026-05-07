class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lr = 0
        rr = len(matrix) - 1
        mr = lr + (rr - lr) // 2
        while mr + 1 < len(matrix) and lr <= rr:
            if matrix[mr][0] <= target and matrix[mr+1][0] > target:
                break
            elif matrix[mr][0] > target:
                rr = mr - 1
            else:
                lr = mr + 1
            mr = lr + (rr - lr) // 2
        
        l = 0
        r = len(matrix[0]) - 1
        while l <= r:
            m = l + (r - l) // 2
            if matrix[mr][m] < target:
                l = m + 1
            elif matrix[mr][m] > target:
                r = m - 1
            else:
                return True

        return False 