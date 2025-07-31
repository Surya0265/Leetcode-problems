class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp=[[0]*len(matrix[0]) for i in range(len(matrix))]
        def dfs(r,c):
            if dp[r][c]:
                return dp[r][c]
            max_len=1
            directions=[[0,-1],[0,1],[-1,0],[1,0]]
            for dx,dy in directions:
                xdx=r+dx
                ydy=c+dy
                if 0<=xdx<len(matrix) and 0<=ydy<len(matrix[0]) and matrix[xdx][ydy]>matrix[r][c]:
                    length=1+dfs(xdx,ydy)
                    max_len=max(max_len,length)
            dp[r][c]=max_len
            return max_len

        res=0


        






        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res=max(res,dfs(i,j))
        return res
                    