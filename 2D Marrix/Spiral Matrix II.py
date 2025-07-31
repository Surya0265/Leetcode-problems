class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix=[[0]*n for i in range(n)]
        top=0
        bottom=len(matrix)
        left=0
        right=len(matrix[0])
        res=[0]*(n*n)
        k=1
        while left<right and top<bottom:
            for i in range(left,right):
                matrix[top][i]=k
                k+=1
            top+=1
            for i in range(top,bottom):
                matrix[i][right-1]=k
                k+=1
            right-=1
            if  not (left<right and top<bottom):
                break
            for i in range(right-1,left-1,-1):
                matrix[bottom-1][i]=k
                k+=1
            bottom-=1
            for i in range(bottom-1,top-1,-1):
                matrix[i][left]=k
                k+=1
            left+=1
        return matrix
        