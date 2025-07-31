class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix[0])-1
        while l<len(matrix) and r>=0:
            if matrix[l][r]==target:
                return True
            elif matrix[l][r]>target:
                r-=1
            else:
                l+=1
        return False
