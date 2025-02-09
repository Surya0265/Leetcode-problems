class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count={}
        c={}
        if(len(s)!=len(t)): return False

        for ch in s:
              count[ch]=count.get(ch,0)+1
        for ch in t:
              c[ch]=c.get(ch,0)+1
        return c==count