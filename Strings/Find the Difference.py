class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        char_count=Counter(s)
        for i in range(len(t)):
            char_count[t[i]]-=1
            if char_count[t[i]]<0:
                return t[i]

        