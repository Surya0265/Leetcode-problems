def knapsack(weights,values,W,n):
    dp=[[0 for i in range(W+1)] for j in range(n+1)]
    for i in range(1,n+1):
        for w in range(1,W+1):
            if weights[i-1]<=w:
                dp[i][w]=max(values[i-1]+(dp[i-1][w-weights[i-1]]),dp[i-1][w])
            else:
                dp[i][w]=dp[i-1][w]
    return dp[n][W]


n=int(input("enter no of terms:"))
W=int(input("enter weight capacity:"))
weights = list(map(int, input("Enter weights: ").split()))
values = list(map(int, input("Enter values: ").split()))
print("Max value:", knapsack(weights, values, W, n))
