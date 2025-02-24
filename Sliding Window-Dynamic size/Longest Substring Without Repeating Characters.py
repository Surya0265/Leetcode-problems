class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count={}
        l=0
        res=0
        for r in range(len(s)):
            if s[r] in count and count[s[r]]>=l:
                  l=count[s[r]]+1
            count[s[r]]=r
            if res<r-l+1:
                res=r-l+1
        return res
        