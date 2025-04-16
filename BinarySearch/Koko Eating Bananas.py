class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        l=1
        r=max(piles)
        res=r
        while(l<=r):
                mid=(l+r)//2
                count=0
                for p in piles:
                       count+=math.ceil(p/mid)
               
                if count<=h:
                      res=min(res,mid)
                      r=mid-1
                else:
                    l=mid+1
        return res
        