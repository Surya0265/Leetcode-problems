class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        maxi=0
        for i in range(len(number)):
            if number[i]==digit:
                 s=int(number[:i]+number[i+1:])
                 if s>maxi:
                    maxi=s
        return str(maxi)
        