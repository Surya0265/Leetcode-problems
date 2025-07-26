class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        time=0
        fresh=0
        q=deque()
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append([i,j])

        while q and fresh>0:
             for i in range(len(q)):
                r,c=q.popleft()
                for dr,dc in directions:
                    x=r+dr
                    y=c+dc
                    if (x<0 or x>=rows) or (y<0 or y>=cols)  or grid[x][y]!=1:
                        continue
                    q.append([x,y])
                    grid[x][y]=2   
                    fresh-=1
                    
               
             time+=1
        return time if fresh==0 else -1


        