class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        indegree=[0]*numCourses
        for dest,src in prerequisites:
            adj[src].append(dest)
            indegree[dest]+=1


        
        res=[]
     
        q=deque([i for i in range(numCourses) if indegree[i]==0])
        while q:
            node=q.popleft()
            res.append(node)
            for neighbour in adj[node]:
                indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    q.append(neighbour)
        return res if len(res)==numCourses else []
        