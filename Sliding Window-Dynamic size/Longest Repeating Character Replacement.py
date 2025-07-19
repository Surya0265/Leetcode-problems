class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
       count=[0]*26
       max_freq=0
       i=0
       res=0
       for j in range(len(s)):
        count[ord(s[j])-ord('A')]+=1
        max_freq=max(max_freq, count[ord(s[j])-ord('A')])
        while(j-i+1)-max_freq>k:
            count[ord(s[i])-ord('A')]-=1
            i+=1
        res=max(res,j-i+1)
       return res





                
                

        