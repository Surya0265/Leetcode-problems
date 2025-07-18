class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i=0
        j=0
        l=0
        res=0
        while(j<len(nums)):
            if nums[j]==0:
                l+=1
            while(l>k):
                if nums[i]==0:
                    l-=1
                i+=1
            res=max(res,j-i+1)
            j+=1
        return res

    


                    
                  

             
        