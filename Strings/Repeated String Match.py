class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        c=1
        repeated=a
        while len(repeated)<len(b):
            repeated+=a
            c+=1
        if b in repeated:
            return c
        repeated+=a
        if b in repeated:
            return c+1
        return -1
        