class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res=[]
        i=0
        while(i+k<len(s)):
             res.append(s[i:k+i])
             i=k+i
        
        st=s[i:]
        while(len(st)<k):
             st+=fill
        res.append(st)
        return res

        