class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        for i in range(0,len(matrix[0])):
            for j in range(i,len(matrix)):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(0,len(matrix)):
            left=0
            right=len(matrix[0])-1
            while(left<right):
                matrix[i][left],matrix[i][right]=matrix[i][right],matrix[i][left]
                left+=1
                right-=1
        
         


        
