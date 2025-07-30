class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color=[-1]*len(graph)
        for i in range(len(graph)):
         if color[i]==-1:
             color[i]=0
             q=[i]
             while q:
                node=q.pop(0)
                for neighbour in graph[node]:
                    if color[neighbour]==-1:
                        color[neighbour]=1-color[node]
                        q.append(neighbour)
                    elif color[neighbour]==color[node]:
                        return False
        return True
            