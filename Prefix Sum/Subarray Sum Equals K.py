class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mapped={}
        count=0
        cursum=0
        for val in nums:
            cursum+=val
            if(cursum==k):
                count+=1
            if (cursum-k) in mapped:
                count+=mapped[cursum-k]
            if cursum in mapped:
                mapped[cursum]+=1
            else:
                mapped[cursum]=1
        return count

            
        