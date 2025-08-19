class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        res = 0
        for num in nums:
            if num == 0:
                count += 1       
                res += count     
            else:
                count = 0        
        return res
