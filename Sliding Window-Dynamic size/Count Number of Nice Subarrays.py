class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count=defaultdict(int)
        prefix_sum=0
        res=0
        count[0]=1
        for i in range(len(nums)):
            prefix_sum+=nums[i]%2
            res+=count[prefix_sum-k]
            count[prefix_sum]+=1
        return res
        
        