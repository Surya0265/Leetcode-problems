class Solution:
    def firstUniqChar(self, s: str) -> int:
    
        n=len(s)
        map={}
         
        for i in range(n):
            if s[i] not in map:
                map[s[i]]=1
            else:
                map[s[i]]+=1
        for i in range(n):
            if map[s[i]]==1:
                return i
        return -1
        