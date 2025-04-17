class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top=0
        bottom=len(matrix)-1
        
        while(top<=bottom):
             mid1=(top+bottom)//2
             l=0
             r=len(matrix[0])-1
             while(l<=r):
                  mid=(l+r)//2
                  if matrix[mid1][mid]==target:
                         return True
                  elif matrix[mid1][mid]<target:
                         l=mid+1
                  else:
                      r=mid-1
             if matrix[mid1][mid]<target:
                   top=mid1+1
             else:
                  bottom=mid1-1
        return False

             
        
        