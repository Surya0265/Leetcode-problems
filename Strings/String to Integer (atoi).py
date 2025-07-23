class Solution:
    def myAtoi(self, s: str) -> int:
        
        sign=1
        idx=0
        res=0
        while(idx<len(s) and s[idx]==' '):
            idx+=1
        if idx<len(s) and  s[idx]=='-':
           sign=-1
           idx+=1
        elif idx<len(s) and s[idx]=='+':
            idx+=1
        
        while (idx<len(s) and '0'<=s[idx]<='9'):
             res=res*10+(ord(s[idx])-ord('0'))
             idx+=1
        
        res=sign*res
        if res>2**31-1:
            return 2**31-1
        if res<-2**31:
             return  -2**31
        return res