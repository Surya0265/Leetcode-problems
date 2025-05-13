class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        add=sum(nums)
        addv=(n*(n+1))/2
        return int(addv-add)