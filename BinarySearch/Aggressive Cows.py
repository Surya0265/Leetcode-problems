class Solution:
    def aggressiveCows(self, stalls, k):
        arr=stalls
        def check(mid):
            cnt=1
            prev=arr[0]
            for i in range(1,len(arr)):
                if arr[i]-prev>=mid:
                    cnt+=1
                    prev=arr[i]
                
            return cnt>=k
        arr.sort()
        l=1
        r=max(arr)-min(arr)
        res=0
        if len(arr)<k:
            return -1
        while l<=r:
            mid=(l+r)//2
            if check(mid):
                res=mid
                l=mid+1

            else:
                r=mid-1
        return res
        