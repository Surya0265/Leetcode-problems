class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def iscap(cap):
            days_needed=1
            current_w=0
            for w in weights:
                if  current_w+w>cap:
                    days_needed+=1
                    current_w=0
                current_w+=w
            return days_needed<=days
        l=max(weights)
        r=sum(weights)
        while(l<r):
                mid=(l+r)//2
                if iscap(mid):
                    r=mid
                else:
                    l=mid+1
        return l
        