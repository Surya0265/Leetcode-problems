from bisect import bisect_right
class Solution:
    def median(self, mat):
       mini=float('inf')
       maxi=float('-inf')
       c=len(mat[0])
       r=len(mat)
       for i in range(r):
           mini=min(mini,mat[i][0])
           maxi=max(maxi,mat[i][c-1])
       desired=(r*c+1)//2
       l=mini
       h=maxi
       while l<h:
           mid=(l+h)//2
           place=0
           for i in range(r):
               place+=bisect_right(mat[i],mid)
           if place<desired:
               l=mid+1
           else:
               h=mid
       return l
    	