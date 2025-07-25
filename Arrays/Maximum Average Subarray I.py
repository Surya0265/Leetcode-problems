class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sumi=sum(nums[:k])
        maxi=sumi
        for i in range(k,len(nums)):
            sumi=sumi-nums[i-k]+nums[i]
            if maxi<sumi:
                maxi=sumi
        return maxi/k

        