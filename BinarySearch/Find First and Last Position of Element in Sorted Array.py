class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res=[]
        def binarysearch(l,r):
            
             while(l<=r):
                 mid=(l+r)/2
                 if nums[mid]==target:
                       return mid
                 elif nums[mid]<target:
                       return binarysearch(mid+1,r)
                 else: 
                    return binarysearch(l,mid-1)
             return -1



        if len(nums)==1 and nums[0]==target:
             return [0,0]
        mid=binarysearch(0,len(nums)-1)
        if mid==-1:
            return [-1,-1]
        l=0
        r=len(nums)-1
        while(l<=mid):
              if nums[l]==target:
                res.append(l)
                break
              l+=1
        while(r>=mid):
             if nums[r]==target:
                res.append(r)
                break
             r-=1
        return res
                      

        