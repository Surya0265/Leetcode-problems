class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        i,j=entrance
        maze[i][j]='+'
        q=deque([(i,j)])
        ans=0
        while q:
         ans+=1
         for _ in range(len(q)):
          i,j=  q.popleft()
          for a,b in [[0,-1],[0,1],[-1,0],[1,0]]:
                x=i+a
                y=j+b
                if 0<=x<len(maze) and 0<=y<len(maze[0]) and maze[x][y]=='.':
                    if (x==0 or x==len(maze)-1) or(y==0 or y==len(maze[0])-1):
                       return ans
                    q.append((x,y))
                    maze[x][y]='+'
        return -1
          
        