class Solution:
    def reverse(self, x: int) -> int:
        
        sum=0
        temp=abs(x)
        while(temp):
            re=temp%10
            sum=sum*10+re
            temp=temp//10
        if sum<=-2**31 or sum>= 2**31 - 1:
                   return 0
        if x>0:
            return sum
        else:
            return -sum
        

        