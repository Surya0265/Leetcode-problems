class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
       mapped={0:-1}
       s=0
       ans=0
       for i in range(len(nums)):
           if nums[i]==1:
                 s+=1
           else:
                 s-=1
           if s in mapped:
               if i-mapped[s]>ans:
                 ans=i-mapped[s]
           else:
               mapped[s]=i
       return ans

        