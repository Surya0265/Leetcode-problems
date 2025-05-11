class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        part=[]
        def ispali(s,l,r):
            while(l<r):
                if s[l]!=s[r]:
                    return 0
                l+=1
                r-=1
            return 1

        def dfs(i):
            if i>=len(s):
                res.append(part[:])
                return
            else:
                for j in range(i,len(s)):
                    if ispali(s,i,j):
                         part.append(s[i:j+1])
                         dfs(j+1)
                         part.pop()
        dfs(0)
        return res
                    
        