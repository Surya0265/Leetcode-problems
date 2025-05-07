INF=float('inf')
def floyd_warshall(graph):
    n=len(graph)
    dist=[row[:] for row in graph]
    for k in range(n):
        for i in range(n):
            for j in range(n):
              if dist[i][k]+dist[k][j]<dist[i][j]:
                  dist[i][j]=dist[i][k]+dist[k][j]
    return dist
n=int(input("no of rowrs or columns"))
flat_input=list(map(int,input("enter values:").split()))
index=0
graph=[]

for i in range(n):
     row=[]
     for j in range(n):
         weight=flat_input[index]
         if i==j:
             row.append(0)
         elif weight==0:
             row.append(INF)
         else:
             row.append(weight)
         index+=1
     graph.append(row)
     

result=floyd_warshall(graph)
print("shortest paths")
for row in result:

     print(" ".join(str(x)if x!=INF else '-' for x in row))
