
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        
        for i in range(1,len(nums)):
            maxi=0
            for j in range(i):
                if nums[j]<nums[i]:
                    maxi=max(maxi,dp[j])
            dp[i]=maxi+1
        return max(dp)        