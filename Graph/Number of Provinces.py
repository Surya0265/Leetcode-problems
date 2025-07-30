class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(visited,isConnected,curr):
            visited[curr]=True
            for adjacent_city,connected in enumerate(isConnected[curr]):
                if not visited[adjacent_city] and connected:
                     dfs(visited,isConnected,adjacent_city)
        visited=[False]*len(isConnected)
        province=0
        for city in range(len(isConnected)):
            if not visited[city]:
                dfs(visited,isConnected,city)  
                province+=1
        return province      


         