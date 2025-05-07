def optimal_bst(freq):
    n=len(freq)
    totalcost=0
    cost=[[0 for i in range(n+1)]for j in range(n+1)]
    for i in range(1,n+1):
        cost[i][i]=freq[i-1]
    for length in range(2,n+2):
        for i in range(n-length+1):
            j=i+length-1
            cost[i][j]=float('inf')
            totalfreq=sum(freq[i:j+1])
            for r in range(i,j+1):
                left=cost[i][r-1] if r>i else 0
                right=cost[r+1][j] if r<j else 0
                totalcost=left+right+totalfreq
                if totalcost<cost[i][j]:
                    cost[i][j]=totalcost
    return cost[0][n-1]

n = int(input("Enter number of keys: "))
freq = list(map(int, input("Enter search frequencies: ").split()))
print("minimum cost:",optimal_bst(freq))

