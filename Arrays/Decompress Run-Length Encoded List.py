class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res=[]
        i=0
        while(i<=len(nums)-2):
              freq=nums[i]
              while(freq!=0):
                  res.append(nums[i+1])
                  freq-=1
              i+=2
        return res
        