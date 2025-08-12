class Solution:
    def findPages(self, arr, k):
        def check(mid):
            cnt=1
            pagesum=0
            for page in arr:
                if page+pagesum>mid:
                    cnt+=1
                    pagesum=page
                else:
                    
                    pagesum+=page
            return cnt<=k
        l=max(arr)
        r=sum(arr)
        res=-1
        if k>len(arr):
            return -1
        while l<=r:
            mid=(l+r)//2
            if check(mid):
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res
