class Solution:
    def maxProduct(self, nums: List[int]) -> int:
          maxprod=nums[0]
          currmin=nums[0]
          currmax=nums[0]
          for i in range(1,len(nums)):
              temp=max(nums[i],nums[i]*currmin,nums[i]*currmax)
              currmin=min(nums[i],nums[i]*currmin,nums[i]*currmax)
              currmax=temp
              
              if maxprod<currmax:
                   maxprod=currmax
          return maxprod