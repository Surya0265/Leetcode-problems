from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
      char_count=Counter(magazine)
      for s in ransomNote:
        char_count[s]-=1
        if char_count[s]<0:
            return False
      return True