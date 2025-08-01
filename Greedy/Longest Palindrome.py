from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count=Counter(s)
        res=0
        for count in char_count.values():
            res+=count-(count%2)
            res+=((res%2==0) and (count%2==1))
        return res

        