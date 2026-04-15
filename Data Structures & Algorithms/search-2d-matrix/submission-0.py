class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        l, r = 0, row * col - 1
        while l <= r:
            mid = l + (r - l) // 2
            mid_i = mid // col
            mid_j = mid % col
            val = matrix[mid_i][mid_j]
            if target == val:
                return True
            elif target > val:
                l = mid + 1
            else:
                r = mid - 1
        return False
