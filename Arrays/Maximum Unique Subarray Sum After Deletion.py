class Solution:
    def maxSum(self, nums: List[int]) -> int:
       if max(nums)<0:
          return max(nums)
       arr=list(set(nums))
       sumi=0
       for i in range(len(arr)):
           if arr[i]>=0:
              sumi+=arr[i]
       return sumi
       