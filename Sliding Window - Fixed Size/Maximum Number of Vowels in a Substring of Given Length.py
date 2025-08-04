
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
       count=0
       maxi=0
       vowels="aeiou"
       for i in range(k):
        if s[i] in "aeiou":
            count+=1
       maxi=count
       for i in range(k,len(s)):
          if s[i] in vowels:
            count+=1
          if s[i-k] in vowels:
            count-=1
          maxi=max(count,maxi)
       return maxi

        