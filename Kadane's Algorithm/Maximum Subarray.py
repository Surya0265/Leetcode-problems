class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=nums[0]
        maxending=nums[0]
        for i in range(1,len(nums)):
            if maxending+nums[i]>nums[i]:
                maxending=maxending+nums[i]
            else:
                maxending=nums[i]
            if maxending>res:
                res=maxending
        return res
        