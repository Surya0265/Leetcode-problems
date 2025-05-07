def print_board(board):
          for row in board:
               print(" ".join(str(x)for x in row))
               print()
def issafe(board,row,col,n):
     for i in range(row):
          if board[i][col]=='Q':
               return False
     i,j=row,col
     while(i>=0 and j>=0):#upper left diagonal
                if board[i][j]=='Q':
                      return False
                i-=1
                j-=1
         
     i,j=row,col
     while(i>=0 and j<n):#upper right diagonal
                if board[i][j]=='Q':
                      return False
                i-=1
                j+=1
     return True



def board_util(board,row,n):
    
     if row==n:
           print_board(board)
           return
     else:
          
      for col in range(n):
        if issafe(board,row,col,n):
              board[row][col]='Q'
              board_util(board,row+1,n)
              board[row][col]='.'
n=int(input("Enter size"))
board=[['.'for i in range(n)]for j in range(n)]
board_util(board,0,n)

# leetcode solutions
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def board_util(board, row, n):
            if row == n:
                res.append(["".join(r)for r in board])
                return 
            else:

                for col in range(n):
                    if issafe(board, row, col, n):
                        board[row][col] = "Q"
                        board_util(board, row + 1, n)
                        board[row][col] = "."

        def issafe(board, row, col, n):
            for i in range(row):
                if board[i][col] == "Q":
                    return False
            i, j = row, col
            while i >= 0 and j >= 0:  # upper left diagonal
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            i, j = row, col
            while i >= 0 and j < n:  # upper right diagonal
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1
            return True

        board = [["." for i in range(n)] for j in range(n)]
        res=[]
        board_util(board, 0, n)
        return res
      
