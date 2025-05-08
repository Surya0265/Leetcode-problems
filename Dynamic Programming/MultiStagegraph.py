def multistage(graph,n):
    cost=[float('inf')]*n
    path=[-1]*n
    cost[n-1]=0
    for i in range(n-2,-1,-1):
        for j in range(n):
            if graph[i][j]!=0:
                if cost[i]>graph[i][j]+cost[j]:
                    cost[i]=graph[i][j]+cost[j]
                    path[i]=j
    stagepath=[]
    i=0
    while(i!=-1):
        stagepath.append(i)
        i=path[i]
    print("Minimum cost from source to destination:", cost[0])
    print("Path:", " -> ".join(map(str, stagepath)))


n = 8  # number of vertices
graph = [[0, 1, 2, 5, 0, 0, 0, 0],
         [0, 0, 0, 0, 4, 11, 0, 0],
         [0, 0, 0, 0, 9, 5, 16, 0],
         [0, 0, 0, 0, 0, 0, 2, 0],
         [0, 0, 0, 0, 0, 0, 0, 18],
         [0, 0, 0, 0, 0, 0, 0, 13],
         [0, 0, 0, 0, 0, 0, 0, 2],
         [0, 0, 0, 0, 0, 0, 0, 0]]


multistage(graph, n)
