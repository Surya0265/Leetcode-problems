class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        maxi=1
        i=1
        length=1
        while(i<len(nums)):
            if nums[i]>nums[i-1]:
              length+=1
              maxi=max(length,maxi)
              i+=1
            else:
                length=1
                i+=1
        return max(length,maxi)

                 
                 
        