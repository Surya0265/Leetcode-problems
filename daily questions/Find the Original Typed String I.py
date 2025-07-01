class Solution:
    def possibleStringCount(self, word: str) -> int:
           total=0
           i=0
           while(i<len(word)):
                j=i
                while(j<len(word) and word[j]==word[i]):
                    j+=1
                runlength=j-i
                if runlength>=2:
                 total+=runlength-1
                i=j
           return total+1
