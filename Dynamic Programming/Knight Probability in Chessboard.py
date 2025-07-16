class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp=[[[0 for i in range(k+1)] for i in range(n)] for j in range(n)]
        directions=[[1,2],[2,1],[-1,2],[1,-2],[-1,-2],[-2,1],[-2,-1],[2,-1]]
        for i in range(n):
            for j in range(n):
                dp[i][j][0]=1.0
        for move in range(1,k+1):
            
            for i in range(n):
                for j in range(n):
                    curr=0.0
                    for d in directions:
                        u=i+d[0]
                        v=j+d[1]
                        if 0<=u<n and 0<=v<n:

                           curr+=dp[u][v][move-1]/8.0
                    dp[i][j][move]=curr
        return dp[row][column][k]

        