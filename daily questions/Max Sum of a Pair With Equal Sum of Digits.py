class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        maxmap=defaultdict(list)
        maxv=0
        s=0
        nums=sorted(nums,reverse=True)
        for i in range(len(nums)):
            s= sum(int(j) for j in str(nums[i]))
            if(len(maxmap[s])<2):
                     maxmap[s].append(nums[i])
           
        for values in maxmap.values():
             if(len(values)==2 and sum(values)>maxv):
                 maxv=sum(values)
        if maxv==0:
            return -1
        return maxv
                 


        