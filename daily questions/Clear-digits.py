class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        for i in s:
            if(i.isdigit()):
                stack.pop()
            else:
                stack.append(i)
        stack=''.join(stack)
        return stack
        