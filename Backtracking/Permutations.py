class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        ans=[]
        def perm(nums,res):
            if not nums:
                ans.append(res[:])
                return
            else:
                for i in range(len(nums)):
                    curr=nums[i]
                    res.append(nums[i])
                    nums.pop(i)
                    perm(nums,res)
                    res.pop()
                  
                    nums.insert(i,curr)
        perm(nums,res)
        return ans