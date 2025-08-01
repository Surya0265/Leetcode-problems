class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start=-1
        end=-2
        max_seen=nums[0]
        min_seen=nums[-1]
        for i in range(len(nums)):
            max_seen=max(max_seen,nums[i])
            if nums[i]<max_seen:
                end=i
        for i in range(len(nums)-1,-1,-1):
            min_seen=min(min_seen,nums[i])
            if nums[i]>min_seen:
                start=i
        return end-start+1
        