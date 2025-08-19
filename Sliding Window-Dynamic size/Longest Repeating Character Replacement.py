class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i=0
        m={}
        maximum=0
        j=0
        while j<len(s):
             m[s[j]]=m.get(s[j],0)+1
             maxi=max(m.values())
            
             if (j-i+1)-maxi<=k:
                maximum=max(maximum,j-i+1)
             else:
                if s[i] in m:
                  m[s[i]]=m.get(s[i],0)-1
                i+=1
             j+=1
       
        return maximum