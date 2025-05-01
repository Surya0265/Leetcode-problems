class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        sum=0

        temp=x
        while(temp):
            re=temp%10
            sum=sum*10+re
            temp=temp//10
        if x==sum:
            return True
        else:
            return False
        
       
        