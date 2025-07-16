class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for i in num:
            while(stack and k>0 and int(stack[-1])>int(i)):
                stack.pop()
                k-=1
            stack.append(i)
        if k:
            stack=stack[:-k]
        result="".join(stack).lstrip('0')
        return result if result else "0"
        