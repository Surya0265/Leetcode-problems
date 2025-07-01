class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s)<=1:
            return s
        dp=[[False]*len(s)for i in range(len(s))]
        for i in  range(len(s)):
            dp[i][i]=True
        start=0
        maxlength=1
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=True
                start=i
                maxlength=2
        for length in range(3,len(s)+1):
            for i in range(len(s)-length+1):
               j=i+length-1
               if s[i]==s[j] and dp[i+1][j-1]:
                     dp[i][j]=True
                     if length>maxlength:
                        maxlength=length
                        start=i

        return s[start:start+maxlength]
