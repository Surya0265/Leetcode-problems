def getCount(n):
    dp=[[[0 for i in range(3)]for i in range(4)]for i in range(n+1)]
    for i in range(4):
        for j in range(3):
            dp[1][i][j]=1
    dp[1][3][0]=0
    dp[1][3][2]=0
    ans=0
    directions=[[0,0],[-1,0],[0,-1],[0,1],[1,0]]
    for k in range(2,n+1):
        for i in range(4):
            for j in range(3):
                if i==3 and(j==0 or j==2):
                        continue
                for d in directions:
                    dx,dy=i+d[0],j+d[1]
                    
                    if 0<=dx<4 and 0<=dy<3:
                         if dx==3 and (dy==0 or dy==2):
                              continue
                         dp[k][i][j]+=dp[k-1][dx][dy]

    for i in range(4):
        for j in range(3):
            if i==3 and(j==0 or j==2):
                        continue
            ans+=dp[n][i][j]
    return ans

if __name__ == "__main__":
    n = int(input("Enter the number of digits (n): "))
    result = getCount(n)
    print(f"Total possible numbers of length {n}: {result}")
