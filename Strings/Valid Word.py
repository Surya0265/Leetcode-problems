class Solution:
    def isValid(self, word: str) -> bool:
        v=0
        c=0
       
        if len(word)<3:
            return False
        for s in word:
            if not ((65<=ord(s)<=90) or (97<=ord(s)<=122) or (48<=ord(s)<=57)):
                return False
            if s.isalpha() and s in "aeiouAEIOU":
                if v==0:
                    v=1
            if s.isalpha() and s not in  "aeiouAEIOU":
                 if c==0:
                    c=1
        if v==1 and c==1:
            return True
        else:
            return False
            
        