class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i=0
        j=0
        count=0
        g.sort()
        s.sort()
        while(i<len(g) and j<len(s)):
            if g[i]<=s[j]:
                count+=1
                i+=1
                j+=1
            else:
                j+=1
        return count
    
        