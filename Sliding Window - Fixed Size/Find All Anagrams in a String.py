class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        scount,pcount={},{}
        if len(p)>len(s): return []
        res=[]
        for i in range(len(p)):
            pcount[p[i]]=1+pcount.get(p[i],0)
            scount[s[i]]=1+scount.get(s[i],0)
        if pcount==scount: 
                res.append(0)
        l=0
       
        for r in range(len(p),len(s)):
            scount[s[r]]=1+scount.get(s[r],0)
            scount[s[l]]-=1
            if scount[s[l]]==0:
               scount.pop(s[l])
            l+=1
            if scount==pcount:
              res.append(l)
    
        return res