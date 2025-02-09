class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count={}
        for i in range(len(nums)):
            if(nums[i] in count and abs(i-count[nums[i]])<=k):
                      return True
            count[nums[i]]=i
        return False
        