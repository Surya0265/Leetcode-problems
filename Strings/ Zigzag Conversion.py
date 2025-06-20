class Solution:
    def convert(self, s: str, numRows: int) -> str:
       
     if numRows==1:
      return s
     else:
       arr=[[] for i in range(numRows)]
       row=0
       flag=False
       for i in range(len(s)):
          arr[row].append(s[i])
          if(row==0 or row==numRows-1):
                flag=not flag
          row=row+(1 if flag else -1)
    
     res="".join(char for row in arr for char in row)
     return res

        
        