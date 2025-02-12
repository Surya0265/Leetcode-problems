class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]: return 0
        nums=set(nums)

        longest=0
        
        for num in nums:
            if num-1 not in nums:
                streak=1
                while num+1 in nums:
                    streak=streak+1 
                    num+=1
                longest=max(longest,streak)
        return longest
                