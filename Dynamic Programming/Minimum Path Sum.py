class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp=[[0]*len(grid[0])for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
             if i==0 and j==0:
                dp[i][j]=grid[i][j]
             elif j==0 and i>0:
                dp[i][j]=grid[i][j]+dp[i-1][j]
             elif i==0 and j>0:
                dp[i][j]=grid[i][j]+dp[i][j-1]
             else:
                dp[i][j]=grid[i][j]+min(dp[i-1][j],dp[i][j-1])
        return dp[len(grid)-1][len(grid[0])-1]      