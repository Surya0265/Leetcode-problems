class Solution:
    def reverseVowels(self, s: str) -> str:
        left=0
        right=len(s)-1
        s=list(s)
        while(left<right):
            if s[left].lower() in "aeiou" and s[right].lower() in "aeiou":
                  s[left],s[right]=s[right],s[left]
                  left+=1
                  right-=1
            elif s[left].lower() in "aeiou" :
                   right-=1
            else:
                left+=1
        return "".join(s)
    