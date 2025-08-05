class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
     count=0
     left=0
     zero_count=0
     maxi=0
     for right in range(len(nums)):
        if nums[right]==0:
            zero_count+=1
        while zero_count>1:
             if nums[left]==0:
                zero_count-=1
             left+=1
        maxi=max(maxi,right-left)
     return maxi


        