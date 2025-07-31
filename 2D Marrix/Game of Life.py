class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def live_count(r,c):
            live=0
            for i in range(r-1,r+2):
                for j in range(c-1,c+2):
                    if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
                        continue
                    if abs(board[i][j])==1 and (i,j)!=(r,c):
                        live+=1
            return live
        for i in range(len(board)):
            for j in range(len(board[0])):
                neighbour_count=live_count(i,j)
                if board[i][j]==1 and (neighbour_count<2 or neighbour_count>3):
                    board[i][j]=-1
                elif board[i][j]==0 and neighbour_count==3:
                    board[i][j]=2
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]>0:
                    board[i][j]=1
                else:
                    board[i][j]=0


        