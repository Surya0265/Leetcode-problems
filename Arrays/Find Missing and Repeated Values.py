class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        sum=0
        m={}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                sum+=grid[i][j]
                if grid[i][j] not in m:
                    m[grid[i][j]]=1
                else:
                    m[grid[i][j]]+=1
        res=[]
        val=len(grid)*len(grid)
        acs=(val*(val+1))//2
        for i in m:
            if m[i]==2:
                 res.append(i)
                 res.append(abs(sum-acs-i))
                 
                 break
        return res
        